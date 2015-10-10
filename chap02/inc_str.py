#!/usr/bin/env python

def inc_str(text='AAAA'):
    try:
        if not text.isalpha():
            raise ValueError
        OrdA = ord('A')
        OrdZ = ord('Z')
        changed = False
        values = [ord(c) for c in reversed(text.upper())]

        for i in range(len(values)):
            if values[i] < OrdZ:
                values[i] += 1
                changed = True
                break
            elif values[i] == OrdZ:
                values[i] = OrdA
        if not changed:
            values = [OrdA] + values
       
    except ValueError:
        values = []

    return ''.join([chr(v) for v in reversed(values)])

def main():
    print inc_str('A')
    print inc_str('Z')
    print inc_str('AM')
    print inc_str('AZ')
    print inc_str('BA')
    print inc_str('BZ')
    print inc_str('ZZA')
    print inc_str('ZZZ')
    print inc_str('AAAA')
    print inc_str('AAAZ')
    print inc_str('ABC2')
    print inc_str('ZZZZ')

if __name__ == '__main__':
    main()