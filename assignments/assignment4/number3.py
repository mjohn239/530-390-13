#!/usr/bin/env python

import number2

def pow2(n):
  N = len(n)
  for i in range(N):
    n[i] = n[i] - 1
    n[i] |= n[i] >> 1
    n[i] |= n[i] >> 2
    n[i] |= n[i] >> 4
    n[i] |= n[i] >> 8
    n[i] |= n[i] >> 16
    n[i] = n[i] + 1
    return n

g = [1,1,0,0,0,0,0,0,0,0,0]
h = [0,0,0,0,1,1,1,0,0,0,0]

g_fixed = pow2(g)
h_fixed = pow2(h)

corr = number2.correlation(g_fixed,h_fixed)
print(corr)

