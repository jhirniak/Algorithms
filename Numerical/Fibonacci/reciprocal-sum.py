#!/usr/bin/python

import sys

def sum(p):
    s = 0.0; i0 = 1.0; i1 = 1.0
    for i in range(p):
        s += 1/i0
        t = i1; i1 += i0; i0 = t
    return s

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print sum(int(sys.argv[1]))
    else:
        print "Expected argument, number of iterations."
