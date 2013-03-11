#!/usr/bin/python2.7
# coding: utf-8
#
# python-hacks: A bunch of small hacks and snippets that I found useful.

def getSpectrum(y,Fs):
    from numpy import arange
    from numpy.fft import fft
    """
    Does the FFT of signal y, sampled at Fs samples per second,
    and returns a list of tuples (frequency,value).
    
    Mostly based upon 
    http://glowingpython.blogspot.com.br/2011/08/how-to-plot-frequency-spectrum-with.html
    """
    n = len(y) # length of the signal
    k = arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(n/2)] # one side frequency range

    Y = fft(y)/n # fft computing and normalization
    Y = Y[range(n/2)]
    return zip(frq, abs(Y))


def unit_step(x):
    from numpy import asarray
    return asarray(x>=0,dtype=float)

def agm(x,y,eps=1e-11):
    from math import sqrt

    if a*g < 0:
	    raise ValueError
    [a, g] = [(x+y)/2.0,sqrt(x*y)]
    while(abs(a-g) > eps):
        [a,g] = [(a+g)/2.0,sqrt(a*g)]
		        
    return a
