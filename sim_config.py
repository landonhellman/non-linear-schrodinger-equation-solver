import numpy as np
global pi; pi=np.pi
from scipy.fftpack import fft, ifft, fftshift, ifftshift, fftfreq
from helper_functions import *

# Simulation Parameters for the Graphs
class SIM_config:
    def __init__(self,N,dt):
        self.number_of_points=N
        self.time_step=dt
        t=np.linspace(0,N*dt,N)
        self.t=t-np.mean(t)

        self.tmin=self.t[0]
        self.tmax=self.t[-1]

        self.f=getFreqRangeFromTime(self.t)
        self.fmin=self.f[0]
        self.fmax=self.f[-1]
        self.freq_step=self.f[1]-self.f[0]

sim_config=SIM_config(N,dt)

# More Constants
amplitude = 1
duration = 2**7*sim_config.time_step
offset = 0
testPulse=GaussianPulse(t, amplitude, duration, offset)

f=getFreqRangeFromTime(t)