#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

def jacobi(u,f,dx,Nx,Ny,itmax):
  x = np.zeros(Nx*Ny)
  for j in range(Ny):
    for i in range(Nx):
      x[i+j*Nx] = u[i+j*Nx]
  for it in range(itmax):
    for j in range(1,Ny-1):
      for i in range(1,Nx-1):
        x[i+j*Nx] = 0.25 * (x[(i-1) + j*Nx] \
                          + x[(i+1) + j*Nx] \
                          + x[i + (j-1)*Nx] \
                          + x[i + (j+1)*Nx] \
                          - dx*dx*f[i + j*Nx])
  return x

Lx = 10
Ly = 4
Nx = 55
Ny = 55

dx = 0.1
dy = 0.1

d2dx2 = 1/(dx*dx)

u = np.zeros(Nx*Ny)
f = np.zeros(Nx*Ny)

# set forcing
i = np.floor(0.5*Nx)
j = np.floor(0.5*Ny)
f[i + j*Nx] = 1

# boundary conditions
for j in range(Ny):
  i = 0
  u[i+j*Nx] = 1
  i = Nx-1
  u[i+j*Nx] = 0
for i in range(Nx):
  j = 0
  u[i+j*Nx] = 0
  j = Ny-1
  u[i+j*Nx] = 0

# Jacobi iteration
u = jacobi(u,f,dx,Nx,Ny,1000)

# plot
u_plot = np.zeros([Nx,Ny])
f_plot = np.zeros([Nx,Ny])
for j in range(Ny):
  for i in range(Nx):
    u_plot[i,j] = u[i+j*Nx]
    f_plot[i,j] = f[i+j*Nx]

x = np.zeros([Nx+1,Ny+1])
y = np.zeros([Nx+1,Ny+1])
for j in range(Ny+1):
  for i in range(Nx+1):
    x[i,j] = -0.5*dx + i*dx
    y[i,j] = -0.5*dy + j*dy

plt.pcolormesh(x,y,u_plot,edgecolors="black")
plt.colorbar()
plt.show()

