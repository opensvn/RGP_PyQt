#!/usr/bin/env python

class EmptyStackError(Exception):
    pass

class Stack(object):
    def __init__(self):
        self.__stack = []

    def __len__(self):
        '''
        >>> s = Stack()
        >>> len(s)
        0
        >>> s.push(3)
        >>> s.push(4)
        >>> len(s)
        2
        >>> s.pop()
        4
        >>> len(s)
        1
        >>> s.pop()
        3
        >>> len(s)
        0
        '''

        return len(self.__stack)

    def __str__(self):
        print self.__stack

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        try:
            if len(self.__stack) == 0:
                raise EmptyStackError
            return self.__stack.pop()
        except EmptyStackError, e:
            print e

    def top(self):
        try:
            if len(self.__stack) == 0:
                raise EmptyStackError
            return self.__stack[-1]
        except EmptyStackError, e:
            print e

if __name__ == '__main__':
    import doctest
    doctest.testmod()
