#!/usr/bin/python
import sys

def p2(sum):
    ps = []
    x = 1
    while (sum > 0):
        if (sum % 2):
            ps.insert(0, x)
        x = x * 2  # Multiply by 2. Is this a bug?
        sum = sum >> 1 # Do a shift.
    # Print the powers.
    for x in ps:
        print x
    return ps

if __name__ == '__main__':
    # TODO Convert sys.arvg[1] into an integer.
    value = int(sys.argv[1])
    p2(value)

