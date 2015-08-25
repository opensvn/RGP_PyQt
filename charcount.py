#!/usr/bin/env python

def charcount(text):
    d = {}
    for c in "abcdefghijklmnoqprstuvwxyz":
        d[c] = 0
    d['whitespace'] = 0
    d['others'] = 0
    for c in text.lower():
        if c in d:
            d[c] += 1
        elif c in " \n\v\f\r":
            d['whitespace'] += 1
        else:
            d['other'] += 1
    return d

stats = charcount("Exceedingly Edible")
print stats
