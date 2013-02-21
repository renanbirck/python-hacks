#!/usr/bin/python2.7
# coding: utf-8
#
# python-hacks: A bunch of small hacks and snippets that I found useful.



def getSpectrum(y,Fs):
    """
    Does the FFT of signal y, sampled at Fs samples per second,
    and returns a list of tuples (frequency,value).
    """
    n = len(y) # length of the signal
    k = arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(n/2)] # one side frequency range

    Y = fft(y)/n # fft computing and normalization
    Y = Y[range(n/2)]
    return zip(frq, abs(Y))

