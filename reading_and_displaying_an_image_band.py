# -------------------------------------------------------------------------------
# Name:        Reading and Displaying an Image Band
#
# Purpose:  Read, display a raster image band using python
#
#
# Author:      Osca Mwongera
#
# Created:     08/04/2021
# Copyright:   (c) 2021 Osca Mwongera
# Licence:     MIT License
# -------------------------------------------------------------------------------
import numpy as np
import sys
from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly
import matplotlib.pyplot as plt

gdal.UseExceptions()


def display(file, band_number):
    gdal.AllRegister()
    try:
        dataset = gdal.Open(file, GA_ReadOnly)
    except RuntimeError as e:
        raise e
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    bands = dataset.RasterCount
    image = np.zeros((bands, rows, cols))
    for b in range(bands):
        band = dataset.GetRasterBand(b + 1)
        image[b, :, :] = band.ReadAsArray(0, 0, cols, rows)
    dataset = None

    band = image[band_number-1, :, :]
    mn = np.amin(band)
    mx = np.amax(band)
    plt.imshow((band-mn)/(mx-mn), cmap='gray')
    plt.show()


if __name__ == '__main__':
    file = sys.argv[1]
    band_number = int(sys.argv[2])
    display(file, band_number)
