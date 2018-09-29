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
"""

import numpy as np
import pandas as pd
import h5py

def restoreH5Py(name):
    whatever = h5py.File(name, 'r')
    testGroup = whatever.get('test')
    return np.array(testGroup.get('block0_values'))

def restorePandas(name):
    return pd.read_hdf(name, key='test', mode='r')

restoredDataFrame = restorePandas('store.h5')