#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 14:31:06 2018

@author: pedro
"""
import pandas as pd
import numpy as np

def restorePandas(path, key): #puxa na forma de um dataframe do pandas
    return pd.read_hdf(path, key, mode='r')

def bootstrapping(array, n=None):
    if n == None:
        n = len(array)
    resample = np.floor(np.random.rand(n)*len(array))
    return array.iloc[resample]

restoredDataFrame = restorePandas('store.h5', 'test')
resampledDataFrame = bootstrapping(restoredDataFrame)