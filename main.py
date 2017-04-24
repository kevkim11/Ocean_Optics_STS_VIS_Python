# import seabreeze and explicitly pyseabreeze which is pyusb
import seabreeze
seabreeze.use('pyseabreeze')
import seabreeze.spectrometers as sb

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import time

from drawnow import drawnow

from IPython import display
import pylab as pl

# fig = plt.figure()
# plot = fig.add_subplot(111)

fig1, ax, = plt.subplots()
plt.ion()

ar_of_in = []

def my_plotter(ax, y):
    ln1 = ax.plot(y, '-b')
    ax.xlabel('bin')
    ax.ylabel('intensities/counts')
    ax.legend()
    return ln1

def makeFig():
    plt.plot(ar_of_in, 'r-')

def plot_intensity(ax, colors=['b']):
    x = np.linespace(0, 1, 100)
    if ax.lines:
        for line in ax.lines:
            line.set_xdata(x)
            y = np.random.random(size=(100,1))
            line.set_ydata(y)
    else:
        for color in colors:
            y = np.random.random(size=(100,1))
            ax.plot(x,y,color)


devices = sb.list_devices()

spec = sb.Spectrometer(device=devices[0])
spec.integration_time_micros(integration_time_micros=10000)

print devices
print spec

ar_of_wavelength = spec.wavelengths()

# while(1):
#     ar_of_intensities = spec.intensities()
#     print ar_of_intensities
#     ax.plot(ar_of_wavelength, c="blue", label='intensities')
#     plt.pause(1)
#
# while (1):
#     ar_of_in = spec.intensities()
#     # a = np.array(ar_of_intensities)
#     print ar_of_in
#     drawnow(makeFig)
#     plt.pause(1.0)

# write to csv file
with open('broken_pixel.csv', 'wb') as f:
    writer = csv.writer(f)
    while (1):
        ar_of_in = spec.intensities()
        # a = np.array(ar_of_intensities)
        print ar_of_in
        writer.writerow(ar_of_in)
        drawnow(makeFig)
        plt.pause(1.0)


    # print ar_of_wavelength
    #
    # #Plot the wavelength and intensities from the spectrometer
    # fig2 = plt.figure()
    # plot2 = fig2.add_subplot(111)
    #
    #
    #
    # plot2.plot(x_axis_wavelength, ar_of_wavelength, c="red", label='wavelength')
    #
    # plt.show()

