from constants import *

# Fiber Configurations/Constants.
class Fiber_config:
    def __init__(self,nsteps,L,gamma,beta2,alpha_dB_per_m):
        self.nsteps=nsteps
        self.ntraces = self.nsteps+1
        self.Length=L
        self.dz=L/nsteps
        self.zlocs=np.linspace(0,L,self.ntraces)
        self.gamma=gamma
        self.beta2=beta2
        self.alpha_dB_per_m=alpha_dB_per_m
        self.alpha_Np_per_m = self.alpha_dB_per_m*np.log(10)/10.0

fiber=Fiber_config(nsteps,Length,gamma,beta2,alpha_dB_per_m)