# FOURIER TRANSFORM: 
import scipy.fft 
fft = scipy.fft.fft(samples)
frequencies = scipy.fft.fftfreq(fft.size, 1/sample_rate)
plt.plot(x=scipy.fft.fftshift(frequencies), 
        y=scipy.fft.fftshift(np.abs(fft)))
plt.show() 


##########################################
import numpy as np
import scipy.io.wavfile
import scipy.fft

sample_rate_1, samples_1 = scipy.io.wavfile.read("./260.wav")
fft_1 = scipy.fft.fft(samples_1)
frequencies_1 = scipy.fft.fftfreq(len(fft_1), 1/sample_rate_1)

#simple plot: 
plt.plot(frequencies_1, np.abs(fft_1))

# nicer plot (without the line following the x-axis, during the "jump" from pos to neg): 
plt.plot(scipy.fft.fftshift(frequencies_1), 
        scipy.fft.fftshift(np.abs(fft_1)))

plt.show() 

print(fft_1.shape, samples_1.shape)