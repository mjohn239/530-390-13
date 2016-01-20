#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def euler_diffusion(u,D,dt,dx,F):
  Nx = len(u)
  tmp = np.zeros(Nx)
  Ddtdx2 = D*dt/(dx*dx)
  for j in range(1,Nx-1):
    tmp[j] = u[j] + Ddtdx2*(u[j+1]-2*u[j]+u[j-1]) - F*dt
  return tmp

D = 1
F = -1
T = 0.1
L = 1
U = 1
mu = 1
Ny = 100
dy = L / (Ny - 1)
dt = 0.5 * dy * dy
Nt = round(T/dt + 1)

t = np.zeros(Nt)
y = np.zeros(Ny)
u = np.zeros([Nt,Ny])
V = np.zeros(Ny)

for i in range(Ny):
  y[i] = i*dy
  u[0,i] = 0
  V[i] = (U * y[i]) / mu + 2 / L

i = 1
while t[i-1] + dt <= T:
  t[i] = t[i-1] + dt
  u[i,:] = euler_diffusion(u[i-1,:],D,dt,dy,F)
  u[i,0] = 0
  u[i,Ny-1] = 0
  i = i + 1

x = y + 2

plt.plot(V,y,u[np.floor(Nt),:],y,u[np.floor(Nt/2),:],y,u[np.floor(Nt/4),:],y,u[np.floor(Nt/8),:],y,x,y)
plt.show()

