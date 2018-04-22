from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import os
from numpy.fft import fftfreq, fft, ifft
from constants import *


def main():
    for file in os.listdir(directory):
        print("Parsing file " + file)
        image = misc.imread('{dir}\\{file}'.format(dir=directory, file=file), flatten=True).astype('float64')
        plt.imshow(image)
        plt.show()

if __name__ == "__main__":
    main()
