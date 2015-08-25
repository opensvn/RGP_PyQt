#!/usr/bin/env python

class Item(object):
    def __init__(self, artist, title, year=None):
        self.__artist = artist
        self.__title = title
        self.__year = year

    def artist(self):
        return self.__artist

    def setArtist(self, artist):
        self.__artist = artist

    def title(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def year(self):
        return self.__year

    def setYear(self, year):
        self.__year = year

    def __str__(self):
        year = ""
        if self.__year is not None:
            year = " in %d" % self.__year
        return "%s by %s%s" % (self.__title, self.__artist, year)

class Painting(Item):
    def __init__(self, artist, title, year=None):
        super(Painting, self).__init__(artist, title, year)

class Sculpture(Item):
    def __init__(self, artist, title, year=None, material=None):
        super(Sculpture, self).__init__(artist, title, year)
        self.__material = material

    def material(self):
        return self.__material

    def setMaterial(self, material):
        self.__material = material

    def __str__(self):
        materialString = ""
        if self.__material is not None:
            materialString = " (%s)" % self.__material
        return "%s%s" % (super(Sculpture, self).__str__(),
                materialString)

class Title(object):
    def __init__(self, title):
        self.__title = title

    def title(self):
        return self.__title

def main():
    a = Painting('Cecil Collins', 'The Sleeping Fool', 1943)
    print a
    b = Sculpture('Auguste Rodin', 'The Secret', 1925, 'bronze')
    print b

    items = []
    items.append(Painting('Cecil Collins', 'The Poet', 1941))
    items.append(Sculpture('Auguste Rodin', 'Naked Balzac', 1917, 
        'plaster'))
    items.append(None)
    items.append(Title('Eternal Springtime'))
    items.append(None)

    #try:
    #    for item in items:
    #        print item.title()
    #except AttributeError:
    #    pass
    for item in items:
        if hasattr(item, 'title') and callable(item.title):
            print item.title()

if __name__ == '__main__':
    main()
