#!/usr/bin/env python

class EmptyStackError(Exception):
    pass

class Stack(object):
    def __init__(self):
        '''
        >>> s = Stack()
        >>> s.push(1)
        >>> s.top()
        1
        >>> s.push(2)
        >>> s.pop()
        2
        >>> s.top()
        1
        >>> s.pop()
        1
        >>> s.top()
        Traceback (most recent call last):
        ...
        EmptyStackError
        >>> s.pop()
        Traceback (most recent call last):
        ...
        EmptyStackError
        '''
        self.__items = []

    def pop(self):
        if len(self.__items) == 0:
            raise EmptyStackError

        return self.__items.pop()

    def top(self):
        if len(self.__items) == 0:
            raise EmptyStackError

        return self.__items[-1]

    def push(self, item):
        self.__items.append(item)

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        '''Returns a string representation of the stack's contents

        >>> s = Stack()
        >>> s.push(1)
        >>> s.push(2)
        >>> s.push('x')
        >>> print s
        [1, 2, 'x']
        '''
        return '[%s]' % ', '.join(['%r' % x for x in self.__items])

if __name__ == '__main__':
    import doctest
    doctest.testmod()