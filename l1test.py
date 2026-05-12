# nécessite le module colorado

# python3 l1test.py [-v] <source_code>.py [-f <test_suite>]
#   -v : verbose, details of successful test appear
#   -f : file name with a test suite inside. Tests are executed on the code of <ource_code>.py according to function names.
# python3 l1test.py -v exemple.py
# python3 l1test.py exemple.py -f exemple.test
# python3 l1test.py -v exemple.py -f exemple.test

import thonnycontrib
from thonnycontrib.backend.evaluator import Evaluator
import thonnycontrib.backend.l1test_backend
from thonny.plugins.cpython_backend.cp_back import MainCPythonBackend
import thonnycontrib.backend.doctest_parser 
from thonnycontrib.backend.doctest_parser import ExampleWithExpected, ExampleWithoutExpected
import thonnycontrib.backend.ast_parser
from thonnycontrib.backend.ast_parser import L1DocTest
import thonnycontrib.backend.verdicts
from thonnycontrib.backend.verdicts.ExceptionVerdict import ExceptionVerdict 
from colorama import Fore

import inspect
import tempfile
import os
import sys

GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
RESET = Fore.RESET
LIGHTYELLOW = Fore.LIGHTYELLOW_EX
        
class MockBackend(MainCPythonBackend):
    """
    Fake backend.
    """
    def __init__(self):
        ...

    def send_message(self, msg) -> None:
        ...

# register backend
thonnycontrib.backend.l1test_backend.BACKEND = MockBackend()


def l1test_to_org(filename: str, test_file_name = "", source: str="", verbose=False):
    """
    Returns the tests of the file `filename` in org format.
    If `source` is not empty, it is used instead of reading the file.
    If `verbose` is True, the details of the tests are printed.

    Parameters:
    filename : the name of the file to test
    test_file_name : the name of the file containing the tests
    source : the source code of the file to test
    verbose : if True, the details of the tests are printed

    """
    abstract = {'total': 0,
                'success': 0,
                'failures': 0,
                'errors': 0,
                'empty': 0}

    if source == "":
        with open(filename, 'rt') as fin:
            source = fin.read()
    evaluator = Evaluator(filename=filename,
                          source=source)
    
    if test_file_name != '' :
        with open(test_file_name, 'r') as f: # plus compliqué que ça, fichier à trouver
            source = f.read()
    tests = evaluator.evaluate(source)
    n = len(tests)
    abstract['total'] = n
    res = ""
    for test in tests:
        examples = test.get_examples()
        res_examples = ""
        nb_test, nb_test_ok = 0, 0
        empty = True
        not_success = False
        for example in examples:
            verdict = test.get_verdict_from_example(example)
            if isinstance(example, ExampleWithExpected):
                nb_test += 1
                if verdict.isSuccess():
                    nb_test_ok += 1
                    abstract['success'] += 1
                else:
                    not_success = True
                    abstract['failures'] += 1
                empty = False
            if isinstance(verdict, ExceptionVerdict):
                abstract['errors'] += 1
                empty = False
            if verbose or not verdict.isSuccess():
                if not_success:
                    res_examples += f"** {RED}{verdict}{RESET}\n\n"
                else:
                    res_examples += f"** {verdict}\n\n"
            if not verdict.isSuccess():
                res_examples += f"   {verdict.get_details()}\n\n"
        if not empty:
            if not_success:
                res += f"* {RED}{test.get_name()}{RESET} ~ {nb_test_ok}/{nb_test} passed\n\n"
            else:
                res += f"* {GREEN}{test.get_name()}{RESET} ~ {nb_test_ok}/{nb_test} passed\n\n"   
        else:
            abstract['empty'] += 1
            res += f"* {LIGHTYELLOW}{test.get_name()}{RESET}\n\n No test found !\n\n"
        res += res_examples
    res = f"Tests run : {abstract['total']}\n{GREEN}Success:{RESET} {abstract['success']}, \
{RED}Failures:{RESET} {abstract['failures']}, {RED}Errors:{RESET} {abstract['errors']}, \
{LIGHTYELLOW}Empty:{RESET} {abstract['empty']}\n\n" + res
    return res

def testmod(modulename: str):
    """
    mimic the doctest.testmod function
    for `modulename` module
    """
    print(l1test_to_org(modulename))

def interprete_command_line(command_ln : list[str]):      # A modifier
    """
    Interpret the command line to see the test to print depending on the arguments.
    Here are the different possibilities :
    - python3 l1test.py [file.py] : print the tests of the file.py
    - python3 l1test.py -v [file.py] : print the tests of the file.py with details
    - python3 l1test.py [file.py] -f [test_file] : print the tests of the file.py with the tests of the test_file
    - python3 l1test.py -v [file.py] -f [test_file] : print the tests of the file.py with the tests of the test_file with details

    Parameters :
    command_ln : list[str] : the list of arguments of the command line
    """
    if len(command_ln) == 2:                  # Exécuter la commande suivante pour tester : python3 l1test.py exemple.py
        if command_ln[1].endswith(".py"):
            print(l1test_to_org(command_ln[1]))
        else:
            print("Error : the file to test has to be a python file")

    elif len(command_ln) == 3:
        if command_ln[1] == "-v":             # Exécuter la commande suivante pour tester : python3 l1test.py -v exemple.py
            if command_ln[2].endswith(".py"):
                print(l1test_to_org(command_ln[2], verbose=True))
            else:
                print("Error : the file to test has to be a python file")
    elif len(command_ln) == 4:                # Exécuter la commande : python3 l1test.py exemple.py -f exemple.test
        if command_ln[2] == "-f":
            if command_ln[1].endswith(".py"):
                print(l1test_to_org(command_ln[1], command_ln[3]))
            else:
                print("Error : the file to test has to be a python file")
    elif len(command_ln) == 5:                # Exécuter la commande : python3 l1test.py -v exemple.py -f exemple.test
        if command_ln[1] == "-v" and command_ln[3] == "-f":
            if command_ln[2].endswith(".py"):
                print(l1test_to_org(command_ln[2], command_ln[4], verbose=True))
            else:
                print("Error : the file to test has to be a python file")


if __name__ == "__main__":
    interprete_command_line(sys.argv)
