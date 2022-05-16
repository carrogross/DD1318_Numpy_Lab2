import numpy as np
from mathplotlib import pyplot as plt 
import scipy.io.wavfile 

sample_rate_1, samples_1 = scipy.io.wavfile.read("./260.wav")
sample_rate_2, samples_2 = scipy.io.wavfile.read("./piano.wav")


print(samples_1.shape, sample_rate_1, len(samples_1) / sample_rate_1)
print(samples_2.shape, sample_rate_2, len(samples_2) / sample_rate_2)
#exit()


# to compute the timestamps: 
times_1 = np.linspace(0, len(samples_1) / sample_rate_1, len(samples_1), endpoint=False)
plt.plot(times_1, samples_1)
times_2 = np.linspace(0, len(samples_2) / sample_rate_2, len(samples_2), endpoint=False)
plt.plot(times_2, samples_2)


# plot without timestamp
#plt.plot(samples_1)


plt.show()


# DOUBLE the frequency => higher pitch: 
scipy.io.wavfile.write("./text.wav", sample_rate_1 * 2, samples_1)

# HALF the frequency => lower pitch: 
scipy.io.wavfile.write("./text.wav", sample_rate_1 // 2, samples_1)


