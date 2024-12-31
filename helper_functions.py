from constants import *

#Changes Time Domain to Frequency Domain
def getFreqRangeFromTime(time):
    return fftshift(fftfreq(len(time), d=time[1]-time[0]))

def getPower(amplitude):
    return np.abs(amplitude)**2

def getEnergy(time_or_frequency,amplitude):
    return np.trapz(getPower(amplitude),time_or_frequency)

def GaussianPulse(time,amplitude,duration,offset):
    return amplitude*np.exp(- ((time-offset)/(duration))**2/2)*(1+0j)

# Frequency to Time Domain
def getSpectrumFromPulse(time,pulse_amplitude):
    pulseEnergy=getEnergy(time,pulse_amplitude)
    f=getFreqRangeFromTime(time)
    dt=time[1]-time[0]

    spectrum_amplitude=fftshift(fft(pulse_amplitude))*dt
    spectrumEnergy=getEnergy(f, spectrum_amplitude)

    err=np.abs((pulseEnergy/spectrumEnergy-1))

    return spectrum_amplitude

def getTimeFromFrequency(frequency):
    return fftshift(fftfreq(len(frequency), d=frequency[1]-frequency[0]))

# Time to Frequency Domain
def getPulseFromSpectrum(frequency,spectrum_amplitude):
    spectrumEnergy=getEnergy(frequency,spectrum_amplitude)
    time=getTimeFromFrequency(frequency)
    dt=time[1]-time[0]

    pulse=ifft(ifftshift(spectrum_amplitude))/dt
    pulseEnergy=getEnergy(time,pulse)
    err=np.abs((pulseEnergy/spectrumEnergy-1))
    return pulse

def GaussianSpectrum(frequency,amplitude,bandwidth):
    time=getTimeFromFrequency(frequency)
    return getSpectrumFromPulse(time, GaussianPulse(time, amplitude, 1/bandwidth, 0))