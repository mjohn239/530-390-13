#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import time
import fft
import gilman-hall.jpg
import improc.py

PI = 2 * np.arcsin(1)
#N = 64
#L = 2 * PI
#dx = L / (N-1)
#x = np.zeros(N)
#f = np.zeros(N)
#y = np.zeros(2*N)
#
#for i in range(N):
#  x[i] = i * dx
#  f[i] = i
#  y[2*i] = np.sin(x[i]) + np.sin(4.*x[i]) # just change the 4?
#  y[2*i+1] = 0
#
#fft.plot_c(x,y)
#y= fft.fft_slow(y,1.)
#fft.plot_c(f[:0.5*N],y[:N])
#y= fft.fft_slow(y,-1.)
#fft.plot_c(x,y)
#
#fft.fft(y,1.)
#fft.plot_c(f[:0.5*N],y[:N])
#fft.fft(y,-1.)
#plt.show()

img = improc.rgb_to_gray_lum(improc.read("gilman-hall.jpg"))
data_real = img[:,0,0]
N = len(data_real)
N2 = fft.pow2(N)
x = np.zeros(N2)
L = N
L2 = N2
data = np.zeros(2*N2)
gaus = np.zerps(2*N2)

signma = 2.*PI
dsigma = 1./ (sigma*sigma)
C = 1./ (np.sqrt(2.*PI)*sigma)
for i in range(N2):
  x[i] = i
  if i < N:
    data[2*i] = data_real[i]
    data[2*i+1] = 0
  gaus[2*i] = C * np.exp(-x[i]*x[i]*dsigma*0.5)
  gaus[2*i] = gaus[2*i] + C * np.xp(-(x[i]-L2)*(x[i]-L2)*dsigma*0.5)
  gaus[2*i+1] = 0
  I = I + gaus[2*i]
for i in range(N2):
  gaus[2*i] = gaus[2*i] / I
