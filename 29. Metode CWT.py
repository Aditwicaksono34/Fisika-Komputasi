import numpy as np
import pywt
import matplotlib.pyplot as plt

Fs = 44100.0  #Samples per second
tclip = 10e-3
nos = int(Fs*tclip)  #No of samples in 10ms
tpoints = np.linspace(0, 10e-3, nos) #Time points
x = np.cos(2*np.pi*500*tpoints)  #cos(2*pi*f*t) signal

scales = np.arange(1, 21, 1)  #No. of scales=20
x[87:89] = 0  #Giving discontinuity
x[307:309] = 0  #Giving discontinuity

coef, freqs = pywt.cwt(x, scales, 'gaus4')  # Finding CWT using gaussian wavelet

# Plotting scalogram
plt.figure(figsize=(15, 10))
plt.imshow(abs(coef), extent=[0, 10e-3, 20, 1], interpolation='bilinear', cmap='copper',
           aspect='auto', vmax=abs(coef).max(), vmin=abs(coef).max())
plt.gca().invert_yaxis()
plt.yticks(np.arange(1, 21, 1))
plt.xticks(np.arange(0, nos/Fs, nos/(20*Fs)))
plt.show()

# Plotting
plt.figure(figsize=(15, 10))
plt.plot(tpoints, x)
plt.grid(color='gray', linestyle=':', linewidth=0.5)
plt.show()