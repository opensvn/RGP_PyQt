#!/usr/bin/env python

import bisect

class OrderedDict(object):
    def __init__(self, dictionary=None):
        self.__keys = []
        self.__dict = {}
        if dictionary is not None:
            if isinstance(dictionary, OrderedDict):
                self.__dict = dictionary.__dict.copy()
                self.__keys = dictionary.__keys[:]
            else:
                self.__dict = dict(dictionary).copy()
                self.__keys = sorted(self.__dict.keys())

    def getAt(self, index):
        return self.__dict[self.__keys[index]]

    def setAt(self, index, value):
        self.__dict[self.__keys[index]] = value

    def __getitem__(self, key):
        return self.__dict[key]

    def __setitem__(self, key, value):
        if key not in self.__dict:
            bisect.insort_left(self.__keys, key)
        self.__dict[key] = value

    def __delitem__(self, key):
        i = bisect.bisect_left(self.__keys, key)
        del self.__keys[i]
        del self.__dict[key]

    def get(self, key, value=None):
        return self.__dict.get(key, value)

    def setdefault(self, key, value):
        if key not in self.__dict:
            bisect.insort_left(self.__keys, key)
        return self.__dict.setdefault(key, value)

    def pop(self, key, value=None):
        if key not in self.__dict:
            return value
        i = bisect.bisect_left(self.__keys, key)
        del self.__keys[i]
        return self.__dict.pop(key, value)

    def popitem(self):
        item = self.__dict.popitem()
        i = bisect.bisect_left(self.__keys, item[0])
        del self.__keys[i]
        return item

    def has_key(self, key):
        return key in self.__dict

    def __contains__(self, key):
        return key in self.__dict

    def __len__(self):
        return len(self.__dict)

    def keys(self):
        return self.__keys[:]

    def values(self):
        return [self.__dict[key] for key in self.__keys]

    def items(self):
        return [(key, self.__keys[key]) for key in self.__keys]

    def __iter__(self):
        return iter(self.__keys)

    def iterkeys(self):
        return iter(self.__keys)

    def itervalues(self):
        for key in self.__keys:
            yield self.__dict[key]

    def iteritems(self):
        for key in self.__keys:
            yield key, self.__dict[key]

    def copy(self):
        dictionary = OrderedDict()
        dictionary.__keys = self.__keys[:]
        dictionary.__dict = self.__dict.copy()
        return dictionary

    def clear(self):
        self.__keys = []
        self.__dict = {}

    def __repr__(self):
        pieces = []
        for key in self.__keys:
            pieces.append("%r: %r" % (key, self.__dict[key]))
        return "OrderedDict({%s})" % ", ".join(pieces)

def main():
    d = OrderedDict(dict(s=1, a=2, n=3, i=4, t=5))
    print repr(d)
    d2 = OrderedDict({2:'a', 3:'m', 1:'x'})
    print `d2`

if __name__ == '__main__':
    main()
