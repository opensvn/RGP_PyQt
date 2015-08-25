#!/usr/bin/env python

def integer(number):
    try:
        num = int(float(number))
    except ValueError, e:
        num = 0
    return num

print integer(4.5)
print integer(32)
print integer("23")
print integer("-15.1")
print integer("tonsils")
