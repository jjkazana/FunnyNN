'''
Take all data and return results of apllying Fast Fourier Transform
to each channel data

Takes 3D array-like object where indexes means [epoch][channel][data_point]
and a callback function, more below


Returns 3D numpy array where indexes means [epoch][channel][frequency]
frequency indices are between 0 and 40 



Callback function takes channel and returns it changed (or not) in whatever 
way user wants 

'''
from numpy.fft import fft
from numpy import zeros, abs

def FourierTransform(data, callback=lambda x:x, low = 0, high = 40):
    epochs = len(data)
    chanels = len(data[0])
    ret = zeros( (epochs, chanels, high-low) )

    for epoch in range(0,epochs):
        print("Calculating FFT of epoch: ", epoch)
        for chanel in range(0,chanels):
            ret[epoch,chanel] = abs(fft(data[epoch,chanel])[low:high])

    return ret


