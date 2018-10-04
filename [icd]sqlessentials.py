#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:06:47 2018

https://www.dataquest.io/blog/python-pandas-databases/
aprendi a mexer com isso aqui, peguei os dados também dali


@author: pedro
"""

import sqlite3
import pandas as pd
from sqlalchemy import create_engine

def createDataBase (pathName, data, tableName, chunkSize):    
    engine = create_engine(pathName, echo = False)
    data.to_sql(tableName, con=engine, chunksize=chunkSize)
    
def readDataBaseTable (dataBase, tableName, indexCol):
    connection = sqlite3.connect(dataBase)
    table = pd.read_sql("SELECT * from %s" %tableName, connection, index_col=indexCol)
    connection.close()
    return table
    
def updateDataBase (data, dataBase, tableName, chunkSize):
    connection = sqlite3.connect(dataBase)
    data.to_sql(tableName, con=connection, if_exists='replace', chunksize=chunkSize)
    connection.close()

def deleteTable(dataBase, tableName):
    connection = sqlite3.connect(dataBase)
    cursor = connection.cursor()
    statement = "DROP TABLE %s" %tableName
    cursor.execute(statement)
    cursor.close()
    connection.close()
    
    

df1 = pd.read_hdf('store.h5', 'alpha', 'r')
#df2 = pd.read_hdf('store.h5', 'beta')

#createDataBase ('sqlite:///test.db', df1.sample(10), 'dailySample1', 250)
updateDataBase(df1.sample(8), "test.db", 'dailySample2', 250)
updateDataBase(df1.sample(10), "test.db", 'dailySample1', 250)
#deleteTable('test.db', 'dailySample2')
dfA = readDataBaseTable('test.db', 'dailySample2', 'index')

#RASCUNHOS
connection = sqlite3.connect("flights.db") #connection normal para sqlite
df = pd.read_sql_query("select * from airlines limit 5;", connection)
connection.close()
#usando o pandas para pegar 5 linhas aereas
