#!/usr/bin/python3
# -*- coding: utf-8 -*-

n = int(input())
loopCount = 0
maxn = n

# TODO: run the loop

while n != 1 :
    loopCount += 1
    if n % 2 == 0 :
        n = n // 2
    else:
        n = n * 3 + 1
        maxn = max(n, maxn)

# TODO: print total number of step
print(loopCount)

# TODO: print the max number encountered in the loop
print(maxn)