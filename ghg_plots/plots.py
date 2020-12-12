#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sources
# 
# CO2
# ftp://data.iac.ethz.ch/CMIP6/input4MIPs/UoM/GHGConc/CMIP/yr/atmos/UoM-CMIP-1-1-0/GHGConc/gr3-GMNHSH/v20160701/mole_fraction_of_carbon_dioxide_in_air_input4MIPs_GHGConcentrations_CMIP_UoM-CMIP-1-1-0_gr3-GMNHSH_0000-2014.csv
temp_infile = 'avtemp.dat'
#co2_infile = 'co2.dat'


# Temperature Data
# source "https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data"
tempdat = pd.read_csv(temp_infile)
tempdat2 = tempdat.iloc[135:,:]

date = tempdat.dt
date2 = tempdat2.dt
avtemp = tempdat.AverageTemperature
avtemp2 = tempdat2.AverageTemperature


#print(avempt2.dt)
# CO2 Data
#co2dat = pd.read_csv(co2_infile)
#co2dat = co2dat.iloc[1880:,:]
#co2year = co2dat.year
#co2conc = co2dat.co2

# Gas Data
gasdat = pd.read_csv('greenhousegases.dat')
gasdat = gasdat.iloc[1880:,:]
print(gasdat.head())
# Plotting

# plt.title("Scatter plot of Global Average Temperature by Year")
# plt.xlabel("Year")
# plt.ylabel("Global Average Temperature (C)")
# plt.scatter(date,avtemp)
# plt.show()

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1.plot(date2,avtemp2)
# ax1.set_ylabel('Global Average Temperature (C)')
# 
# ax2 = ax1.twinx()
# ax2.plot(date2,avtemp2)
# ax2.set_ylabel("Global Average CO2 level (mmol)")
# for tl in ax2.get_yticklabels():
#     tl.set_color('r')
# 
# plt.show()

"""
ax = tempdat2.plot(x='dt',y='AverageTemperature',legend=False)
ax2 = ax.twinx()
ax.set_ylabel("Temperature (C)")
ax2.set_ylabel("CO2 Concentration (mmol)")
ax.set_title("Average Global Temperature and CO2 Concentration By Year")
ax.set_xlabel("date")
co2dat.plot(x='year',y='co2',ax=ax2,color='r',legend=False)
ax.figure.legend(loc='upper center')
plt.show()
"""
ax = tempdat2.plot(x='dt',y='AverageTemperature',legend=False)
ax.set_ylabel('Temperature (C)')
gasdat.plot(x='year',y=list(gasdat.drop(columns='year').columns))
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()




