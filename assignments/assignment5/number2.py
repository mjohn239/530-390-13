#!/usr/bin/env python

import numpy as np

PI = 2.*np.arcsin(1)

def trap(func, a, b, N):
  h = (b-a) / (N-1)
  S = 0.5*(func(a) + func(b))
  x = a + h
  for j in range(1,N-1):
    S = S + func(x)
    x = x + h
  S = S*h
  return S

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

def lin(x):
  return x

def quad(x):
  return x*x

def eleven(x):
  return x*x*x*x*x*x*x*x*x*x*x

def twelve(x):
  return x*x*x*x*x*x*x*x*x*x*x*x

def exp(x):
  return np.exp(x)

a = 0
b = 1

# y = x
print(trap(lin,a,b,10))
print(trap(lin,a,b,100))
print(trap(lin,a,b,1000))
[x,w] = gauss_leg(a,b,1)
print(gauss_quad(lin,x,w))
[x,w] = gauss_leg(a,b,2)
print(gauss_quad(lin,x,w))
[x,w] = gauss_leg(a,b,6)
print(gauss_quad(lin,x,w))

# y = x^2
print(trap(quad,a,b,10))
print(trap(quad,a,b,100))
print(trap(quad,a,b,1000))
[x,w] = gauss_leg(a,b,1)
print(gauss_quad(quad,x,w))
[x,w] = gauss_leg(a,b,2)
print(gauss_quad(quad,x,w))
[x,w] = gauss_leg(a,b,6)
print(gauss_quad(quad,x,w))

# y = x^11
print(trap(eleven,a,b,10))
print(trap(eleven,a,b,100))
print(trap(eleven,a,b,1000))
[x,w] = gauss_leg(a,b,1)
print(gauss_quad(eleven,x,w))
[x,w] = gauss_leg(a,b,2)
print(gauss_quad(eleven,x,w))
[x,w] = gauss_leg(a,b,6)
print(gauss_quad(eleven,x,w))

# y = x^12
print(trap(twelve,a,b,10))
print(trap(twelve,a,b,100))
print(trap(twelve,a,b,1000))
[x,w] = gauss_leg(a,b,1)
print(gauss_quad(twelve,x,w))
[x,w] = gauss_leg(a,b,2)
print(gauss_quad(twelve,x,w))
[x,w] = gauss_leg(a,b,6)
print(gauss_quad(twelve,x,w))

# y = e^x
print(trap(exp,a,b,10))
print(trap(exp,a,b,100))
print(trap(exp,a,b,1000))
[x,w] = gauss_leg(a,b,1)
print(gauss_quad(exp,x,w))
[x,w] = gauss_leg(a,b,2)
print(gauss_quad(exp,x,w))
[x,w] = gauss_leg(a,b,6)
print(gauss_quad(exp,x,w))

