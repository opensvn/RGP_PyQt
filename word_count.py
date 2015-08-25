#!/usr/bin/env python

from sys import argv

d = dict()

with open(argv[1]) as f:
    a = []
    for line in f.readlines():
        a.extend(line.split())
    for s in a:
        if (d.has_key(s)):
            d[s] += 1
        else:
            d[s] = 1

for key in d.keys():
    print key, d[key]
