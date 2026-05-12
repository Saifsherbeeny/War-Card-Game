#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`apqueue` module

:author: `FIL - Faculté des Sciences et Technologies -
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2015, september
:last revision: 2026, March

A module for queue data structure.

:Provides:

* class ApQueue

and methods

* `enqueue`
* `dequeue`
* `is_empty`
"""
from typing import TypeVar

T = TypeVar('T')


class ApQueueEmptyError(Exception):
    """Exception for empty stacks."""

    def __init__(self, msg):
        """Initialise a queue error."""
        self.message = msg


class ApQueue():
    """
    Implementation of a queue.

    $$$ ap_queue = ApQueue()
    $$$ ap_queue.is_empty()
    True
    $$$ ap_queue.enqueue(1)
    $$$ ap_queue.is_empty()
    False
    $$$ ap_queue.enqueue(2)
    $$$ tmp = deepcopy(ap_queue)
    $$$ tmp == ap_queue
    True
    $$$ str(ap_queue)
    '→2|1→'
    $$$ ap_queue.dequeue()
    1
    $$$ ap_queue.dequeue()
    2
    $$$ ap_queue.is_empty()
    True
    $$e ap_queue.dequeue()
    ApQueueEmptyError
    $$$ tmp == ap_queue
    False
    $$$ tmp == ()
    False
    """

    ARROW = chr(0x2192)

    def __init__(self):
        """Build  a new empty queue."""
        self.__content = []

    def enqueue(self, elt: T):
        """Insert an element elt at the begining of the queue."""
        self.__content.insert(0, elt)

    def dequeue(self) -> T:
        """Return the element on top of self.

        Side effect: self contains an element less
        Precondition: self must be non empty
        """
        if len(self.__content) > 0:
            return self.__content.pop()
        else:
            raise ApQueueEmptyError('empty queue, nothing to dequeue')

    def is_empty(self) -> bool:
        """Return True iff self is empty."""
        return self.__content == []

    def __str__(self) -> str:
        """Return the string representation of this queue."""
        return ApQueue.ARROW + \
            "|".join(str(el) for el in self.__content) + \
            ApQueue.ARROW

    __repr__ = __str__
    
    def __len__(self) -> int:
        """Return the length of this queue."""
        return len(self.__content)

    def __eq__(self, other) -> bool:
        """Return True iff self is identical to other."""
        return isinstance(other, ApQueue) and self.__content == other.__content


if __name__ == '__main__':
    import l1test
    l1test.testmod('apqueue.py')
