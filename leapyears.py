#!/usr/bin/env python

def leapyears(yearlist):
    try:
        for year in yearlist:
            year = int(year)
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                yield year
    except ValueError, e:
        #print e
        pass

l = leapyears([1600, 1604, 1700, 1704, 1800, 1900, 1996, 2000, 2004])
for y in l:
    print y,
print
