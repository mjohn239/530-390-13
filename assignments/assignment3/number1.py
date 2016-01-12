#!/usr/bin/env python

import numpy as np
import random
import time

# selection sort
def selectionsort(A, n):
  for i in range(n):
    m = A[i]
    mj = i
    for j in range(i,n):
      if A[j] < m:
        m = A[j]
        mj = j
    A[mj] = A[i]
    A[i] = m

# merge sort (entry point)
def mergesort(A,n):
  if n > 1:
    m = round(0.5 * n)
    mergesort(A[0:m],m)
    mergesort(A[m:], n-m)
    merge(A,n,m)

# merge
def merge(A,n,m):
  B = np.empty(n)
  i = 0 # first half index
  j = m # second half index
  for k in range(n):
    if j == n:
      B[k] = A[i]
      i = i + 1
    elif i == m:
      B[k] = A[j]
      j = j + 1
    elif A[j] < A[i]:
      B[k] = A[j]
      j = j + 1
    else:
      B[k] = A[i]
      i = i + 1
  for i in range(n):
    A[i] = B[i]

# compare sorting algorithms
def comparesort(N):
  A = np.random.rand(N)
  A2 = np.array(A)
  t0 = time.time()
  selectionsort(A,N)
  t1 = time.time()
  mergesort(A2,N)
  t2 = time.time()
  print(t1 - t0, t2 - t1)

# compare times for different sizes N
comparesort(100)
# selection sort time = 0.001244, merge sort time = 0.001454
comparesort(1000)
# selection sort time = 0.123083, merge sort time = 0.018130
comparesort(10000)
# selection sort time = 12.2384, merge sort time = 0.218801

