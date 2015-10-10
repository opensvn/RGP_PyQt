#!/usr/bin/env python

def integer(number):
    try:
        num = int(round(float(number)))
    except ValueError:
        num = 0
    return num

def main():
    print integer(4.5)
    print integer(32)
    print integer("23")
    print integer("-15.1")
    print integer("tonsils")

if __name__ == '__main__':
    main()