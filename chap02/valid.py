#!/usr/bin/env python

def valid(text, chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    result = []
    for c in text:
        if c in chars:
            result.append(c)
    return ''.join(result)

def main():
    print valid('Barking!')
    print valid('KL754', '0123456789')
    print valid('BEAN', 'abcdefghijklmnopqrstuvwxyz')

if __name__ == '__main__':
    main()
