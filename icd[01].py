#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:04:08 2018

@author: pedro
"""
"""
Esse codigo cobre as questoes de abrir e manipular dados, plotar dados
e obter gráficos interativos. 

Estranhamente, no momento de criar um novo dataframe a partir do original, 
alguns dados "somem", como a Média Diária, por exemplo, isso precisa ser revisto. RESOLVIDO

Tentar uma abordagem diferente, gerar uma nova série a partir das medições diárias,
agrupar a partir de anos hidrológicos. MEDIÇÕES DIÁRIAS FEITAS

"""

import pandas as pd
import numpy as np
import plotly.graph_objs as gr
import plotly.figure_factory as ff
from plotly.offline import plot

mydataframe = pd.read_csv('VAZOES.ZIP', compression='zip', sep=';', 
                          encoding='ISO-8859-1', skiprows=16, parse_dates=['Data'], 
                          dayfirst=True, index_col='Data', decimal = ',' )

mydataframe.index = pd.to_datetime(mydataframe.index)



aux = mydataframe[list(mydataframe.columns[15:46])]

aux = aux.groupby(pd.Grouper(freq='M')).mean()

#preenchendo buracos
for x in range (0, 248):
    if aux.iloc[x].name.daysinmonth == 28:
        for y in range (0,28):
            if pd.isna(aux.iloc[x][y]):
                aux.iloc[x][y] = 0
    elif aux.iloc[x].name.daysinmonth == 29:
        for y in range (0,29):
            if pd.isna(aux.iloc[x][y]):
                aux.iloc[x][y] = 0
    elif aux.iloc[x].name.daysinmonth == 30:
        for y in range (0,30):
            if pd.isna(aux.iloc[x][y]):
                aux.iloc[x][y] = 0
    else:
       for y in range (0,31):
            if pd.isna(aux.iloc[x][y]):
                aux.iloc[x][y] = 0


newdataframe = pd.DataFrame()


for x in range (0,248):
    test = [newdataframe, aux.iloc[x]]
    newdataframe = pd.concat(test, ignore_index=True)
newdataframe.dropna(how='all', inplace=True)
newdataframe = newdataframe.set_index(pd.date_range('1995-01-01', '2015-08-31', freq='D'))
    
del aux, test, x, y #comendo memória a toa

newdataframe = newdataframe.replace(0, np.nan)

def drawGantt(data):
    intervals = []
    d = []
    inter = []
    
    for indexCount, indexValue in data.itertuples():
        if pd.isna(indexValue) == False:
            d.append(indexCount)
        else:
            if d != []:
                intervals.append(d)
            d = []
    for interval in intervals:
        inter.append(dict(Task='Vazao', Start = min(interval), Finish = max(interval)))
        
    fig = ff.create_gantt(inter)
    plot(fig, filename='testGantt.html')


def plotMonthlyMean (data):
    monthlymean = data.groupby([pd.Grouper(freq='M')]).mean()


    trace = gr.Scatter(
            x = monthlymean.index, 
            y = monthlymean[0],
            name = 'Média mensal'
            )

    plot([trace], filename='test')
    
drawGantt(newdataframe)