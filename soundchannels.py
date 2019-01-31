import wave

f = wave.open('osi_sample.wav')
print(f.getnchannels())
print(f.getsampwidth())
print(f.getnframes())

rawdata = bytearray(f.readframes(1000000))
del rawdata[2::4] #Borrado canal derecho - Estereo
del rawdata[2::3]

wavedata = [a + (b << 8) for a, b in zip(rawdata[::2], rawdata[1::2])]

print(rawdata[0])

import pylab
pylab.plot(wavedata)
pylab.show()