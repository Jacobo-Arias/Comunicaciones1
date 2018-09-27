import numpy as np 
import matplotlib.pyplot as plt
#import scipy.ndimage

plt.style.use('ggplot')

def convolve1d(signal, ir):
	'''
	we use the 'same' / 'constant' method for zero padding. 
	'''
	n = len(signal)
	m = len(ir)
	output = np.zeros(n)

	for i in range(n):
		for j in range(m):
			if i - j < 0: continue
			output[i] += signal[i - j] * ir[j]

	return output

def make_square_and_saw_waves(height, start, end, n):
	single_square_wave = []
	single_saw_wave = []
	for i in range(n):
		if start <= i < end:		
			single_square_wave.append(height)
			single_saw_wave.append(height * (end-i) / (end-start))
		else:
			single_square_wave.append(0)
			single_saw_wave.append(0)

	return single_square_wave, single_saw_wave

# create signal and IR
start = 40
end = 60
single_square_wave, single_saw_wave = make_square_and_saw_waves(
	height=10, 
	start=start, 
	end=end, 
	n=100)

# convolve, compare different methods
np_conv = np.convolve(
	single_square_wave, 
	single_saw_wave, 
	mode='same')

convolution1d = convolve1d(
	single_square_wave, 
	single_saw_wave)

'''
sconv = scipy.ndimage.convolve1d(
	single_square_wave, 
	single_saw_wave, 
	mode='constant')
'''

# plot them, scaling by the height
plt.clf()
fig, axs = plt.subplots(5, 1, figsize=(12, 6), sharey=True, sharex=True)

axs[0].plot(single_square_wave / np.max(single_square_wave), c='r')
axs[0].set_title('Single Square')
axs[0].set_ylim(-.1, 1.1)

axs[1].plot(single_saw_wave / np.max(single_saw_wave), c='b')
axs[1].set_title('Single Saw')
axs[2].set_ylim(-.1, 1.1)

axs[2].plot(convolution1d / np.max(convolution1d), c='g')
axs[2].set_title('Our Convolution')
axs[2].set_ylim(-.1, 1.1)

axs[3].plot(np_conv / np.max(np_conv), c='g')
axs[3].set_title('Numpy Convolution')
axs[3].set_ylim(-.1, 1.1)

'''
axs[4].plot(sconv / np.max(sconv), c='purple')
axs[4].set_title('Scipy Convolution')
axs[4].set_ylim(-.1, 1.1)
'''

plt.show()

'''
from scipy.ndimage.filters import convolve as convolve_sci
from pylab import *

N = 100
start=N//8
end = N-start
A = zeros(N)
A[start:end] = 1
B = zeros(N)
B[start:end] = linspace(1,0,end-start)

figure(figsize=(6,7))
subplot(411); grid(); title('Signals')
plot(A)
plot(B)
subplot(412); grid(); title('A*B numpy')
plot(convolve(A,B, mode='same'))
subplot(413); grid(); title('A*B scipy (zero padding and moved origin)')
plot(convolve_sci(A,B, mode='constant', origin=-N//2))
tight_layout()
show()
'''
