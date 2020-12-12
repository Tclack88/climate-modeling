#!/usr/bin/env python3

import pandas as pd

infile = 'globaltempdata.csv'

df = pd.read_csv(infile)

print(df.Country.unique())

tempdat = df[['dt','AverageTemperature']]


print(tempdat.head())
print(tempdat.shape[0])


tempdat.dropna(inplace=True)

def addfrac(x):
    x = x.split('-')
    return int(x[0])

tempdat.dt = tempdat.dt.apply(addfrac)
tempdat = tempdat.groupby('dt',as_index=False).mean() # add on
tempdat.AverageTemperature = tempdat.AverageTemperature.apply(lambda x: round(x,3))


print(tempdat.head())
print(tempdat.shape[0])

tempdat.to_csv("avtemp.dat",index=False)

