#!/usr/bin/env python

import numpy as np

def multiply(A,B):
  N = len(A)
  tmp = np.zeros(N)
  for i in range(N):
    tmp[i] = A[i]*B[i]
  return tmp

def gauss_leg(a, b, N):
  x = np.zeros(N)
  w = np.zeros(N)
  eps = 1.e-14
  m = (N+1) >> 1
  xm = 0.5*(b+a)
  xl = 0.5*(b-a)
  for i in range(m):
    z = np.cos(PI*(i+0.75)/(N+0.5))
    z1 = z + 1.
    while (abs(z-z1) > eps):
      p1 = 1.
      p2 = 0.
      for j in range(N):
        p3 = p2
        p2 = p1
        p1 = ((2.*j+1) * z * p2 - j * p3) / (j+1)
      pp = N * (z * p1 - p2) / (z * z - 1.)
      z1 = z
      z = z1 - p1 / pp
    x[i] = xm - xl*z
    x[N-1-i] = xm + xl*z
    w[i] = 2.*xl / ((1.-z*z) * pp*pp)
    w[N-1-i] = w[i]
  return [x,w]

def gauss_quad(func,x,w):
  N = len(x)
  I = 0
  for i in range(N):
    I = I + w[i]*func(x[i])
  return I

def compute(func1,func2,a,b,n,N):
  tmp1 = np.zeros(N)
  tmp2 = np.zeros(N)
  for i in range(N):
    tmp1[i] = func1(i)
  for j in range(N):
    tmp2[j] = func2(j)
  prod = multiply(tmp1,tmp2)
  [x,w] = gauss_leg(a,b,n)
  ans = gauss_quad(prod,x,w)
  print(ans)

def sin(x):
  return np.sin(x)

def sin2(x):
  return np.sin(2*x)

def sin8(x):
  return np.sin(8*x)

PI = 2.*np.arcsin(1)
N = 10000

a = 0
b = 2*PI
n = 2

compute(sin,sin,a,b,n,N)
compute(sin,sin2,a,b,n,N)
compute(sin2,sin8,a,b,n,N)
compute(sin8,sin8,a,b,n,N)

