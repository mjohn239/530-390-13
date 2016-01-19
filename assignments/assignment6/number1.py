#!/usr/bin/env python

import numpy as np
import random
import matplotlib.pyplot as plt

def create_array(N,beta):
  A = np.zeros(N)
  for i in range(N):
    A[i] = exponential(beta)
  return A

def exp(x):
  return np.exp(x)

def exponential(beta):
  tmp = random.random()
  if tmp == 0:
    tmp = random.random()
  else:
    return -np.log(tmp)/beta

def monte_carlo_1d(func,a,b,N):
  f = 0
  f2 = 0
  L = b-a
  for i in range(N):
    x = a + random.random()*L
    f = f + func(x)
    f2 = f2 + func(x)*func(x)
  f = f / N
  f2 = f2 / N
  I = f / L
  S = np.sqrt((f2 - f*f) / N) * L
  return [I,S]

N = 4 # number of bins
n = 100000

A = create_array(n,2)
plt.figure(1)
plt.hist(A,N)
plt.show()
A_norm = monte_carlo_1d(exp,0,4,10000)
plt.figure(2)
plt.hist(A_norm,N)
plt.show()

