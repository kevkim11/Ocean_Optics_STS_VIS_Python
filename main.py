# import seabreeze and explicitly pyseabreeze which is pyusb
import seabreeze
seabreeze.use('pyseabreeze')
import seabreeze.spectrometers as sb

import matplotlib.pyplot as plt
import pandas as pd
import csv

if __name__ == '__main__':
    devices = sb.list_devices()

    spec = sb.Spectrometer(device=devices[0])
    spec.integration_time_micros(integration_time_micros=10000)

    print devices
    print spec

    ar_of_wavelength = spec.wavelengths()
    ar_of_intensities = spec.intensities()

    print ar_of_wavelength
    print ar_of_intensities

    #Plot the wavelength and intensities from the spectrometer