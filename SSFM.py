from fiber import *
from sim_config import *

def SSFM(fiber:Fiber_config,sim:SIM_config,pulse):

    psi_t = np.zeros((fiber.nsteps+1,sim.number_of_points))*(1+0j)
    psi_w = np.copy(psi_t)
    psi_t[0,:]=pulse
    psi_w[0,:] = getSpectrumFromPulse(sim.t, pulse)

    # Differential Operator
    disp_and_loss=np.exp((1j*fiber.beta2/2*(2*pi*sim.f)**2-fiber.alpha_Np_per_m)*fiber.dz)
    # Nonlinear Operator (excluding some terms)
    nonlinearty=1j*fiber.gamma*fiber.dz
    
    for n in range(fiber.nsteps):
        # Applies Fourier Transform on Pulse, and returns pulse with dispersion/nonlinearity terms applied.
        pulse*=np.exp(nonlinearty*getPower(pulse))
        spectrum = getSpectrumFromPulse(sim.t, pulse)*disp_and_loss
        pulse=getPulseFromSpectrum(sim.f, spectrum)

        psi_t[n+1,:]=pulse
        psi_w[n+1,:]=spectrum
        print(n)

    return psi_t, psi_w

psi_t,psi_w = SSFM(fiber,sim_config,testPulse)