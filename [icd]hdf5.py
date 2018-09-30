#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 16:24:30 2018

@author: pedro
"""

"""
dados do link: https://www.osti.gov/biblio/1223853-brady-geothermal-field-sample-interferogram-hdf5-format
dados do link vazios!!!!!
usei o pandas para gerar um novo treco la tlg

EDIT: peguei dados daqui: https://figshare.com/articles/NEON_Teaching_Data_Imaging_Spectrometer_Data_HDF5/4307183
"""

import numpy as np
import pandas as pd
import h5py

def restoreH5Py(name): #meh
    whatever = h5py.File(name, 'r')
    testGroup = whatever.get('test')
    return np.array(testGroup.get('block0_values'))

def restorePandas(path, key): #puxa na forma de um dataframe do pandas
    return pd.read_hdf(path, key, mode='r')

def readH5Py(path, key): #puxa na forma de um array do Numpy
    whatever = h5py.File(path, 'r')
    test = whatever.get(key)
    return np.array(test)

wavelength = readH5Py('NEONDSImagingSpectrometerData.h5', 'wavelength')
restoredDataFrame = restorePandas('store.h5', 'test')