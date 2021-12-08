from os import path
from scipy.fftpack import fft
from pydub import AudioSegment
from librosa import display
from scipy.io import wavfile as wav

import librosa
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# # files                                                                         
# src = "photograph.mp3"
# dst = "photograph.wav"

# # convert wav to mp3                                                            
# sound = AudioSegment.from_mp3(src)
# sound.export(dst, format="wav")

plt.figure()

# plot frequency graph
mpl.rcParams['agg.path.chunksize'] = 100000
rate, data = wav.read('photograph.wav')
fft_out = fft(data)

# librosa.display.waveplot(y=data, sr=rate)

plt.plot(data, np.abs(fft_out))

# plt.plot(data, np.abs(fft_out))
plt.xlabel("Time")
plt.xlabel("Magnitude")
plt.show()


# # Comments: 
# dont connect the lines
# wider frequency bins (make it resonable)
# visualize in log scale (both x and y)