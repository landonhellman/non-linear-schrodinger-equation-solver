import numpy as np
from scipy.fftpack import fft, ifft, fftshift, ifftshift, fftfreq

N = 2**15
dt = 0.1e-12
t=np.linspace(0,N*dt,N)
t=t-np.mean(t)

# Fiber Constants
alpha_dB_per_m = 0.2e-4
dB_cutoff = -30

#Constants to change
nrange=1000 #typically 600
Length = 1e5
gamma = 10e-3
beta2 = 100e3 * (1e-30)
#nsteps includes number of points along z-axis.
nsteps = 2**8

#Soliton kind of found @ these constants? Not too sure
#nrange=1000 #typically 600
#Length = 1e2
#gamma = 10e-3
#beta2 = 100e3 * (1e-30)
#nsteps = 2**8