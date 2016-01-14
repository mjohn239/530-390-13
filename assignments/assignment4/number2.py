#!/usr/bin/env python

import numpy as np

def fft(data, isign):
  n = len(data) >> 1
  if n < 2 or n & (n-1):
    print("data must be length of a power of two")
    return data
  else:
    nn = n << 1
    j = 1
    for i in range(1,nn,2):
      if j > i:
        tmp = data[i-1]
        data[i-1] = data[j-1]
        data[j-1] = tmp
        tmp = data[i]
        data[i] = data[j]
        data[j] = tmp
      m = n
      while m >= 2 and j > m:
        j = j - m
        m = m >> 1
      j = j + m
    mmax = 2
    while nn > mmax:
      istep = mmax << 1
      theta = isign*2.*PI/mmax
      wtemp = np.sin(0.5*theta)
      wpr = -2.*wtemp*wtemp
      wpi = np.sin(theta)
      wr = 1.
      wi = 0.
      for m in range(1,mmax,2):
        for i in range(m,nn,istep):
          j = i + mmax
          tempr = wr*data[j-1] - wi*data[j]
          tempi = wr*data[j] + wi*data[j-1]
          data[j-1] = data[i-1] - tempr
          data[j] = data[i] - tempi
          data[i-1] = data[i-1] + tempr
          data[i] = data[i] + tempi
        wtemp = wr
        wr = wtemp*wpr - wi*wpi + wr
        wi = wi*wpr + wtemp*wpi + wi
      mmax = istep
    if isign < 0:
      for i in range(2*n):
        data[i] = data[i] / n
    return data


def correlation(A,B):
  fft(A,1.)
  fft(B,1.)
  N = len(A) >> 1
  corr = np.zeros(2*N)
  for i in range(N):
    corr[2*i] = A[2*i]*B[2*i] - A[2*i+1]*B[2*i+1]
    corr[2*i+1] = -1*A[2*i+1]*B[2*i] - A[2*i]*B[2*i+1]
  fft(corr,-1.)
  return corr

