#!/usr/bin/env python

def charcount(text):
    stats = {}
    for c in 'abcdefghijklmnopqrstuvwxyz':
        stats[c] = 0
    stats['whitespace'] = 0
    stats['others'] = 0

    for c in text.lower():
        if c in stats:
            stats[c] += 1
        elif c.isspace():
            stats['whitespace'] += 1
        else:
            stats['others'] += 1

    return stats

def main():
    stats = charcount('Exceedingly Edible')
    print stats

if __name__ == '__main__':
    main()
