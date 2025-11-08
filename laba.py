import numpy as np

class SignalGenerator:
    def __init__(self,frequency,amplitude=1.0):
        self.frequency = frequency
        self.amplitude = amplitude
    def generate(self,time):
        return self.amplitude*np.sin(2*np.pi*self.frequency*time)