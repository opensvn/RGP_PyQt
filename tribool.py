#!/usr/bin/env python

class Tribool(object):
    def __init__(self, state):
        self.__state = state

    def __str__(self):
        print 'Tribool(%s)' % self.__state

    def __repr__(self):
        print 'Tribool(%r)' % self.__state

    def __cmp__(self, Tribool tb):
        return cmp(self.__state, tb.__state)

    def __nonzero__(self):
        if self.__state is None:
            return None
        return self.__state

    def __invert__(self):
        if self.__state is None:
            return None
        return not self.__state

    def __and__(self, Tribool tb):
        if self.__state is None or tb.__state is None:
            return None
        return self.__state & tb.__state

    def __or__(self, Tribool tb):
        if 
