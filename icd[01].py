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
por exemplo, isso precisa ser revisto.
"""

import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as gr

mydataframe = pd.read_csv('VAZOES.ZIP', compression='zip', sep=';', 
                          encoding='ISO-8859-1', skiprows=16, parse_dates=['Data'], 
                          dayfirst=True, index_col='Data', decimal = ',' )

yearmean = mydataframe.groupby([pd.Grouper(freq='Y')]).mean()

trace1 = gr.Scatter(
        x = yearmean.index, 
        y = yearmean['DiaMaxima'],
        name = 'Dia Máxima'
        )
trace2 = gr.Scatter(
        x = yearmean.index, 
        y = yearmean['DiaMinima'],
        name = 'Dia Mínima'
        )

data = [trace1, trace2]
plot(data, filename='test')


"""
Tentar uma abordagem diferente, gerar uma nova série a partir das medições diárias,
agrupar a partir de anos hidrológicos
"""
