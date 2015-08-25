#!/usr/bin/env python

from string import uppercase

def inc_str(text='AAAA'):
    try:
        text = text[::-1]
        i = 0
        carry = 0
        while i < len(text):
            if text[i] not in uppercase:
                raise ValueError
            if i == 0 and text[i] == 'Z':
                carry = 1
                text = text[:i] + 'A' + text[i+1:]
            else:
                if text[i] == 'Z':
                    carry = 1
                    text = text[:i] + 'A' + text[i+1:]
                else:
                    carry = 0
                    c = chr(ord(text[i])+1)
                    text = text[:i] + c  + text[i+1:]
                    break
            i += 1
        if carry == 1:
            text = 'A' + text
        text = text[::-1]
    except ValueError:
        return ''

    return text

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
