"""
Code Reference: 
https://towardsdatascience.com/understanding-audio-data-fourier-transform-fft-spectrogram-and-speech-recognition-a4072d228520

https://stackoverflow.com/questions/23377665/python-scipy-fft-wav-files


"""

from os import path
from scipy.fftpack import fft
from pydub import AudioSegment
from librosa import display
from scipy.io import wavfile as wav # get the api

import librosa
import scipy
import numpy as np
import matplotlib.pyplot as plt

""" ---------------- convert from .mp3 to .wav ----------------"""
# files                                                                         
src = input("Enter the mp3 file with the .mpa extension:")
dst = src[0:-3] + "wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

""" --------------------- data maniputation -------------------- """

file_path = dst
samples, sampling_rate = librosa.load(file_path, sr = None, mono = True, offset = 0.0, duration = None)
# samples: an array of amplitues
# sr = none -> load audio file in its original sampling rate
print("Sample length: ", len(samples))
print("Frequency sampling rate", sampling_rate)

duration = len(samples)/sampling_rate # gives all th seconds
minutes = duration // 60
seconds = duration % 60
print("duration: %02d:%02d" % (minutes, seconds))


""" ------------------- plot time & frequency graph ------------------- """
'''
plt.figure()

# mpl.rcParams['agg.path.chunksize'] = 100000
fs_rate, signal = wav.read("photograph.wav")

chan = len(signal.shape)
if chan == 2:
    signal = signal.sum(axis=1) / 2

time_step = 1.0/fs_rate #sampling interval in time
t = np.arange(0, duration, time_step) # time vector as scipy arange field / numpy.ndarray

FFT = abs(fft(signal))
FFT_side = FFT[range(len(samples)//2)]

# complete fft spectrum
freqs = scipy.fftpack.fftfreq(signal.size, t[1]-t[0])
# scipy.fftpack.fftfreq returns the discrete FT sample frequencies
fft_freqs = np.array(freqs)

#one side (positive) fft spectrum
freqs_side = freqs[range(len(samples)//2)]
fft_freqs_side = np.array(freqs_side)

plt.subplot(2, 2, 1)
p1 = librosa.display.waveplot(y=samples, sr=sampling_rate, color="slateblue")
plt.title("Time-Domain Representation")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(2, 2, 2)
p2 = plt.plot(freqs, FFT, "salmon") # plotting the complete fft spectrum
plt.title("Complete fft Spectrum")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Count dbl-sided')

plt.subplot(2, 2, 3)
p3 = plt.plot(freqs_side, abs(FFT_side), "b") # plotting the positive fft spectrum
plt.title("Positive fft Spectrum")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Count single-sided')

plt.subplot(2, 2, 4)
p4 = plt.specgram(samples, sampling_rate)
plt.title("Spectrogram")
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

plt.show()

'''


# # Comments: 
# dont connect the lines
# wider frequency bins (make it resonable)
# visualize in log scale (both x and y)