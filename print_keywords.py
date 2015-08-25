#!/usr/bin/evn python
#-*- coding: utf-8 -*-

from sys import argv
from math import ceil

def print_keywords(keyword, col):
    row = int(ceil(len(keyword) / float(col)))
    longest = max(len(word) for word in keyword)
    #print longest

    for r in range(row):
        #print r
        for c in range(col):
            index = r + c * row
            if index < len(keyword):
                word = keyword[index]
                spaces = ' ' * (longest - len(word))
                print word + spaces,
            else:
                print '',
        print

def main():
    keyword = []
    with open('cpp_keyword.txt') as f:
        for line in f:
            keyword.extend(line.split())

    col = int(argv[1])
    print_keywords(keyword, col)

if __name__ == '__main__':
    main()
