#!/usr/bin/env python

import random
import numpy as np

def monte_carlo_3d(func,a,b,inregion,N):
  f = 0
  f2 = 0
  Lx = b[0]-a[0]
  Ly = b[1]-a[1]
  Lz = b[2]-a[2]
  for i in range(N):
    x = a[0] + random.random() * Lx
    y = a[1] + random.random() * Ly
    z = a[2] + random.random() * Lz
    if inregion(x,y,z):
      f = f + func(x,y,z)
      f2 = f2 + func(x,y,z) * func(x,y,z)
  f = f / N
  f2 = f2 / N
  I = f * Lx*Ly*Lz
  S = np.sqrt((f2-f*f) / N) * Lx*Ly*Lz
  return [I,S]

def sphere(x,y,z):
  if x*x+y*y+z*z <= 1:
    return True
  else:
    return False

def density(x,y,z):
  return 1.

def xmoment(x,y,z):
  return x

def ymoment(x,y,z):
  return y

def zmoment(x,y,z):
  return z

[w,Sw] = monte_carlo_3d(density,[-0.5,-0.5,-1],[1,1,1],sphere,100000)
[x,Sx] = monte_carlo_3d(xmoment,[-0.5,-0.5,-1],[1,1,1],sphere,100000)
[y,Sy] = monte_carlo_3d(ymoment,[-0.5,-0.5,-1],[1,1,1],sphere,100000)
[z,Sz] = monte_carlo_3d(zmoment,[-0.5,-0.5,-1],[1,1,1],sphere,100000)

print('The COM of the object is: ' , x/w , ', ' , y/w , ', ' , z/w , '.')
