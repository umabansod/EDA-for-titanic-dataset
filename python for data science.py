# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:48:00 2020

@author: shree
"""

import pandas as pd


## whatis series data ( one dimentional data)

data=[1,2,3,4]
series1=pd.Series(data)
print(series1)


type(series1)


series1=pd.Series(data,index=['a','b','c','d'])
print(series1)


## creating a dataframe

data=[1,2,3,4,5]
df=pd.DataFrame(data)
print(df)


df=pd.DataFrame(data,index=['a','b','c','d','e'])
df

## creating dataframe using list
import pandas as pd
dictionary={'fruits':['apples','banana','mangoes'],'counts':[10,20,15]}
df=pd.DataFrame(dictionary)
df





## creating a dataframe using a series

series=pd.series([6,12],index=['a','b'])
df=pd.DataFrame(series)

df

## creating dataframes using numpy array

import numpy as np

numpyarray=np.array([[50000,60000],['John','James']])
df=pd.DataFrame({'name':numpyarray[1],'salary':numpyarray[0]})
df



########################################
# How to perform a Merge operation?
########################################

import pandas as pd
player=['player1','player2','player3']
point=[8,9,7]
title=['Game1','Game2','Game3']
df1=pd.DataFrame({'Player':player,'Points':point,'title':title})
df1



player=['player1','player2','player4']
power=['punch','kick','elbow']
title=['Game1','Game3','Game4']
df2=pd.DataFrame({'Player':player,'power':power,'title':title})
df2

## inner merge
df1.merge(df2,on='Player',how='inner')

