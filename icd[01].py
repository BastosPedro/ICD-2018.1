#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:04:08 2018

@author: pedro
"""
"""
Esse codigo cobre as questoes de abrir e manipular dados, plotar dados
e obter gráficos interativos. Estranhamente, no momento de criar um novo
dataframe a partir do original, alguns dados "somem", como a Média Diária,
por exemplo, isso precisa ser revisto. RESOLVIDO

Tentar uma abordagem diferente, gerar uma nova série a partir das medições diárias,
agrupar a partir de anos hidrológicos MEDIÇÕES DIÁRIAS FEITAS

"""

import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as gr
#import cufflinks as cf #cufflinks bugado?

mydataframe = pd.read_csv('VAZOES.ZIP', compression='zip', sep=';', 
                          encoding='ISO-8859-1', skiprows=16, parse_dates=['Data'], 
                          dayfirst=True, index_col='Data', decimal = ',' )

mydataframe.index = pd.to_datetime(mydataframe.index)


#mydataframe = mydataframe.reindex(pd.date_range('1995-01-01', '2015-08-31', freq = 'M'))
#mesmo settando as variáveis corretas, o reindex anula tudo :/


#conveniência
aux = mydataframe[['Vazao01', 'Vazao02', 'Vazao03', 'Vazao04', 'Vazao05', 'Vazao06',
                   'Vazao07', 'Vazao08', 'Vazao09', 'Vazao10', 'Vazao11', 'Vazao12',
                   'Vazao13', 'Vazao14', 'Vazao15', 'Vazao16', 'Vazao17', 'Vazao18',
                   'Vazao19', 'Vazao20', 'Vazao21', 'Vazao22', 'Vazao23', 'Vazao24',
                   'Vazao25', 'Vazao26', 'Vazao27', 'Vazao28', 'Vazao29', 'Vazao30', 'Vazao31']]

#preenchendo buracos
for x in range (0, 242):
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


auxdataframe = pd.DataFrame()
aux2dataframe = pd.DataFrame()

for x in range (0, 65):
    test = [auxdataframe, aux.iloc[x]]
    auxdataframe = pd.concat(test, ignore_index=True)
auxdataframe.dropna(how='all', inplace=True)
auxdataframe = auxdataframe.set_index(pd.date_range('1995-01-01', '2000-05-31', freq='D'))

for x in range (65, 242):
    test = [aux2dataframe, aux.iloc[x]]        
    aux2dataframe = pd.concat(test, ignore_index=True)       
aux2dataframe.dropna(how='any', inplace=True)
aux2dataframe = aux2dataframe.set_index(pd.date_range('2000-12-01', '2015-08-31', freq='D'))

test = [auxdataframe, aux2dataframe]
newdataframe = pd.concat(test, ignore_index=False)
del aux, auxdataframe, aux2dataframe, test, x, y #comendo memória a toa

monthlymean = newdataframe.groupby([pd.Grouper(freq='M')]).mean()
monthlymean.dropna(how='any', inplace=True) #deixa o gráfico contínuo

trace = gr.Scatter(
        x = monthlymean.index, 
        y = monthlymean[0],
        name = 'Média mensal'
        )

plot([trace], filename='test')