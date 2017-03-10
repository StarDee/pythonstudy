# !/usr/bin/env python3
# -*- coding: utf-8 -*-
def triangles():
    L=[1]
    yield L
    while True:
        L.append(0)#在L尾部补0
        L=[L[i-1]+L[i] for i in range(len(L))]
        yield L

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break