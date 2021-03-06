#!/usr/bin/env python

import sys

pre = None
num = 1

for line in sys.stdin:
    word, count = line.strip().split('\t')
    if pre:
        if word == pre:
            num += int(count)
        else:
            print ("Urgency :%s \t\tCount: %d" % (pre, num))
            num = 1

    pre = word

if num > 1:
    print ("Urgency :%s \t\tCount: %d" % (pre, num))
