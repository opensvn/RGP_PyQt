#!/usr/bin/env python

class Rectangle(object):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def _area(self):
        return self.__width * self.__height

    def _getWidth(self):
        return self.__width

    def _setWidth(self, width):
        self.__width = width

    def _getHeight(self):
        return self.__height

    def _setHeight(self, height):
        self.__height = height

    area = property(fget=_area)
    width = property(fget=_getWidth, fset=_setWidth)
    height = property(fget=_getHeight, fset=_setHeight)

def main():
    rect = Rectangle(5, 4)
    print rect.width, rect.height, rect.area
    rect.width = 6
    print rect.width

if __name__ == '__main__':
    main()
