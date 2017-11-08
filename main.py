# import seabreeze and explicitly pyseabreeze which is pyusb
import seabreeze
seabreeze.use('pyseabreeze')
import seabreeze.spectrometers as sb

import matplotlib.pyplot as plt
import numpy as np
import csv
import time

from drawnow import drawnow

fig1, ax, = plt.subplots()
plt.ion()

ar_of_in = []

# def my_plotter(ax, y):
#     ln1 = ax.plot(y, '-b')
#     ax.xlabel('bin')
#     ax.ylabel('intensities/counts')
#     ax.legend()
#     return ln1

def makeFig():
    plt.plot(ar_of_in, 'r-')

# def plot_intensity(ax, colors=['b']):
#     x = np.linespace(0, 1, 100)
#     if ax.lines:
#         for line in ax.lines:
#             line.set_xdata(x)
#             y = np.random.random(size=(100,1))
#             line.set_ydata(y)
#     else:
#         for color in colors:
#             y = np.random.random(size=(100,1))
#             ax.plot(x,y,color)

# 1) Get a list of devices
devices = sb.list_devices()

# 2) Get the spectrometer from the list of devices
spec = sb.Spectrometer(device=devices[0])
# 3) Set the integration (normally 10000 microseconds, ideally 250 microseconds)
spec.integration_time_micros(integration_time_micros=25000)

print devices
print spec

ar_of_wavelength = spec.wavelengths()
print "!!!!!!!!!!!!!!!!!!!!!!11"
print spec.spectrum()

###### Just to plot the data
# while (1):
#     ar_of_in = spec.intensities(correct_nonlinearity=True)
#     # a = np.array(ar_of_intensities)
#     # print ar_of_in
#     drawnow(makeFig)
#     plt.pause(1)

###### write to csv file and plot data.
with open('broken_pixel.csv', 'wb') as f:
    writer = csv.writer(f)
    while (1):
        ar_of_in = spec.intensities()
        # a = np.array(ar_of_intensities)
        # print ar_of_in
        # writer.writerow(ar_of_in)
        drawnow(makeFig)
        # plt.pause(1.0)

