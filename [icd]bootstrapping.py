#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 14:31:06 2018

@author: pedro
"""
import pandas as pd
import numpy as np
import statsmodels.stats.api as sm


def restorePandas(path, key): #puxa na forma de um dataframe do pandas
    return pd.read_hdf(path, key, mode='r')

def resample_BS(array, sampleNumber, sampleSize=None): #reamostragem
    auxResample = list()
    for count in range(0, sampleNumber):    
        auxResample.append(array.sample(sampleSize))
    resample = np.concatenate(auxResample, axis = 1)
    resample = pd.DataFrame(resample)
    return resample

def bootstrapping(array, n=None): #depreciado, pandas já faz isso aew
    if n == None:
        n = len(array)
    resample = np.floor(np.random.rand(n)*len(array))
    return array.iloc[resample]

restoredDataFrame = restorePandas('store.h5', 'test')
resampledDataFrame = resample_BS(restoredDataFrame, 8, 10)
interval = sm.DescrStatsW(resampledDataFrame.mean()).tconfint_mean()
