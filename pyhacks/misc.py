#!/usr/bin/python2.7
# coding: utf-8
#
# python-hacks: A bunch of small hacks and snippets that I found useful.

def number_of_differences(v1, v2):
    """ Returns the number of differences between arrays, considering order. 
        Not too fast, but not terribly slow either. """
        
    i = 0;
    for el in range(len(v1)):
        if v1[el] != v2[el]:
            i = i+1
    return i
