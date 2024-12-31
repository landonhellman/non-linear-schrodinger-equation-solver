## Credit: https://www.youtube.com/watch?v=xIdozUy9Nas and Nonlinear Fiber Optics by Agrawal
## - Landon Hellman

## This NLSE Solver is for 1+1D Equations, NOT the equation given in Agrawal's book.

import numpy as np
global pi; pi=np.pi

import matplotlib.pyplot as plt
from matplotlib import cm
from sim_config import *
from fiber import *
from SSFM import *

def plotFirstAndLastPulse(matrix,fiber:Fiber_config,sim:SIM_config,nrange:int):
    t=sim_config.t[int(sim_config.number_of_points/2-nrange):int(sim_config.number_of_points/2+nrange)]*1e12
    plt.figure()
    plt.title("The Initial Pulse and Final Pulse")
    plt.xlabel("Time[ps]")
    plt.ylabel("Power[W]")
    plt.plot(t,getPower(matrix[0,int(sim_config.number_of_points/2-nrange):int(sim_config.number_of_points/2+nrange)]),label="Initial Pulse")
    plt.plot(t,getPower(matrix[-1,int(sim_config.number_of_points/2-nrange):int(sim_config.number_of_points/2+nrange)]),label="Final Pulse")
    plt.show()

def plotPulseMatrix3D(matrix,fiber:Fiber_config,sim:SIM_config, nrange:int, dB_cutoff,**kwargs):
  fig,ax = plt.subplots(1,1, figsize=(10,7),subplot_kw={"projection": "3d"})
  plt.title("Pulse Evolution (dB scale)")

  t=sim_config.t[int(sim_config.number_of_points/2-nrange):int(sim_config.number_of_points/2+nrange)]*1e12
  z=fiber.zlocs 
  T_surf, Z_surf=np.meshgrid(t, z)
  P_surf=getPower(matrix[:,int(sim_config.number_of_points/2-nrange):int(sim_config.number_of_points/2+nrange)]  )/np.max(getPower(matrix[:,int(sim_config.number_of_points/2-nrange):int(sim_config.number_of_points/2+nrange)]))
  P_surf[P_surf<1e-100]=1e-100
  P_surf=10*np.log10(P_surf)
  P_surf[P_surf<dB_cutoff]=dB_cutoff
  surf=ax.plot_surface(T_surf, Z_surf, P_surf, cmap=cm.viridis,
                        linewidth=0, antialiased=False)
  ax.set_xlabel('Time [ps]')
  ax.set_ylabel('Distance [m]')
  #fig.colorbar(surf, shrink=0.5, aspect=5)
  plt.show()

if __name__ == "__main__":
  #plotFirstAndLastPulse(psi_w,fiber,SIM_config,nrange)
  plotPulseMatrix3D(psi_w,fiber,SIM_config,nrange,dB_cutoff)