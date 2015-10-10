#!/usr/bin/env python

def leapyears(yearlist):
    try:
        for year in yearlist:
            year = int(year)
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                yield year
    except ValueError:
        pass

def main():
    yearlist = [1600, 1604, 1700, 1704, 1800, 1900, 1996, 2000, 2004]
    for leap_year in leapyears(yearlist):
        print leap_year,
    print

if __name__ == '__main__':
    main()