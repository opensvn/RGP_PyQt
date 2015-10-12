#!/usr/bin/env python

class Dimension(object):
    def area(self):
        raise NotImplementedError, 'Dimension.area()'

    def volume(self):
        raise NotImplementedError, 'Dimension.volume()'

class Triangle(Dimension):
    def area(self):
        pass

def main():
    # d = Dimension()
    # d.area()
    
    t = Triangle()
    t.area()

if __name__ == '__main__':
    main()