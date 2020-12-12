#!/usr/bin/env python3

import pandas as pd


# For proper use, infiles must be named in format: (name_of_gas)data.csv
infile1 = 'co2data.csv'
#infile2 = 'methanedata.csv'
#infile3 = 'sf6data.csv'

# Create dataframe of only year, append gases from each file afterwards
dropcols = ['data_mean_global','data_mean_nh','data_mean_sh']
gases = pd.read_csv(infile1).drop(columns=dropcols)

def merge_gases(infile):
    df = pd.read_csv(infile)
    dropcols = ['year','data_mean_nh','data_mean_sh']
    df = df.drop(columns=dropcols)
    #newname = infile[:-8]+'.dat'
    df = df.rename(columns={'data_mean_global':infile[:-8]})
    df_appended = pd.concat([gases,df],axis=1)#,join='inner')
    #print(gases.head())
    return df_appended

#filelist = [infile1,infile2,infile3]

l = """
c2f6data.csv   c6f14data.csv  nitrousOxidedata.csv
c3f8data.csv   c7f16data.csv                methanedata.csv         sf6data.csv
c4f10data.csv  c8f18data.csv                methylBromidedata.csv
c4f8data.csv   carbonTetraChloridedata.csv  methylChloridedata.csv
c5f12data.csv  co2data.csv                  nf3data.csv
"""

filelist = l.split()


for file in filelist:
    gases = merge_gases(file)

print(gases.head())

gases.to_csv('greenhousegases.dat',index=False)
