#!/usr/bin/env python

class Dimension(object):
    def area(self):
        raise NotImplementedError, 'Dimension.area()'

    def volume(self):
        raise NotImplementedError, 'Dimension.volume()'
