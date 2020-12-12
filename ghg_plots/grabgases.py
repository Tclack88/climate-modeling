#!/usr/bin/env python3

import pandas as pd

infile1 = 'co2data.csv'
infile2 = 'methanedata.csv'
infile3 = 'sf6data.csv'

def grab_data(infile):
    df = pd.read_csv(infile)
    dropcols = ['data_mean_nh','data_mean_sh']
    df = df.drop(columns=dropcols)
    newname = infile[:-8]+'.dat'
    df = df.rename(columns={'data_mean_global':infile[:-8]})
    #print(newname)
    df.to_csv(newname)
    #print(df.head())


filelist = [infile1,infile2,infile3]

for file in filelist:
    grab_data(file)
