#!/usr/bin/env python

import librosa
import os, glob
import numpy, scipy.io

import scipy.io.wavfile;

import pylab;pylab.ion();
import pdb;



def main():
    wavfile = r'data\test1_22050.wav';
    (y,sr) = librosa.load_scipy(wavfile);
    n_fft=2048;
    hop_length=1024;
    S = librosa.stft(y,n_fft=n_fft,hop_length=hop_length);
    abs_S = abs(S);
    C = librosa.feature.chromagram(abs_S,sr);
    pdb.set_trace();

    
if __name__ == "__main__":
    main();
