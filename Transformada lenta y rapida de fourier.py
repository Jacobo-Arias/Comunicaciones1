import numpy as np
import timeit

timeit.timeit()

mycode = '''
def DFT_slow(x):
    
    x = np.asarray(x,dtype = float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N,1))
    w = np.exp(-2j*np.pi*k*n/N)
    return np.dot(w,x)

def FFT(x):
    
    x = np.asarray(x,dtype = float)
    N = x.shape[0]
    if N % 2 > 0:
        raise ValueError("El tamalo de x debe ser potencia de 2")
    elif N <= 32:
        return DFT_slow(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        W = np.exp(-2j*np.pi*np.arange(N)/N)
        #print ('even',X_even,'odd ',X_odd)
        return np.concatenate([X_even + W[:int(N/2)] * X_odd, X_even + W[int(N/2):] *X_odd])

x = np.random.random(1024*32)

np.fft.fft(x) '''

print(timeit.timeit(setup = "import numpy as np",stmt = mycode, number = 1))

'''\n\n FFT:\n',FFT(x),'\n\n np.fftfft(x): \n',np.fft.fft(x)'''