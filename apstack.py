#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`stack` module

:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2015, september
:last revision: 2026, march

A module for stack data structure.

:Provides:

* class ApStack

and methods

* `push`
* `pop`
* `top`
* `is_empty`

:Examples:
"""
from typing import TypeVar

T = TypeVar('T')


class ApStackEmptyError(Exception):
    """Exception for empty stacks."""

    def __init__(self, msg):
        """Initialise une erreur de pile."""
        self.message = msg


class ApStack():
    """
    Une classe représentant une pile.

    $$$ stack = ApStack()
    $$$ stack.is_empty()
    True
    $$$ stack.push(1)
    $$$ stack.is_empty()
    False
    $$$ stack.push(2)
    $$$ str(stack)
    "|2|\\n|1|\\n+-+"
    $$$ tmp = deepcopy(stack)
    $$$ tmp == stack
    True
    $$$ stack.top()
    2
    $$$ stack.pop()
    2
    $$$ stack.top()
    1
    $$$ stack.pop()
    1
    $$$ stack.is_empty()
    True
    $$e stack.pop()
    ApStackEmptyError
    $$$ tmp == stack
    False
    $$$ tmp == ()
    False
    """

    def __init__(self):
        """Build a new empty stack."""
        self.__content = []

    def push(self, el: T):
        """Add el on top of the stack."""
        self.__content.append(el)

    def pop(self) -> T:
        """Return the element on top of self.

        Side effect: self contains an element less
        Précondition : self must be non empty"""
        if len(self.__content) == 0:
            raise ApStackEmptyError('empty stack, nothing to pop')
        return self.__content.pop()

    def top(self) -> T:
        """Return the element on top of self without removing it.

        Précondition : self must be non empty """
        if len(self.__content) == 0:
            raise ApStackEmptyError('empty stack, nothing to pop')
        return self.__content[-1]

    def is_empty(self) -> bool:
        """Return True ssi self is emmpty."""
        return self.__content == []

    def __str__(self) -> str:
        """Return a stack representation."""
        mlen = 1
        if not self.is_empty():
            mlen = max(len(str(el)) for el in self.__content)
        res = []
        for el in self.__content:
            pad = mlen - len(str(el))
            right = pad // 2
            left = pad - right
            res.insert(0, "|" + " " * left + str(el) + " " * right + "|")
        res.append("+" + "-" * mlen + "+")
        return "\n".join(res)

    def __len__(self) -> int:
        """Return the stack length."""
        return len(self.__content)

    def __eq__(self, other) -> bool:
        """Return True iff other is the same stack."""
        return isinstance(other, ApStack) and self.__content == other.__content

    def __repr__(self) -> str:
        """Return the elements of st horizontally.

        Exemple(s) :
        $$$ st = ApStack()
        $$$ repr(st)
        '['
        $$$ for i in range(1, 5): st.push(i)
        $$$ repr(st)
        '[1 2 3 4 '
        """
        if self.is_empty():
            return "["
        else:
            n = self.pop()
            res = f"{repr(self)}{n} "
            self.push(n)
            return res


if __name__ == '__main__':
    import l1test
    l1test.testmod('apstack.py')
