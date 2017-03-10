# !/usr/bin/env python3
# -*- coding: utf-8 -*-
def hanoi(n,a,b,c):
    if (n == 1):
        print('%s -->%s' % (a, c))
    else:
        hanoi(n - 1, a, c, b)
        print('%s -->%s' % (a, c))
        hanoi(n - 1, b, a, c)
hanoi(4,'A','B','C')