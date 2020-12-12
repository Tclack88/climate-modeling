#!/usr/bin/env python3

l = """
c2f6data.csv   c6f14data.csv                globaltempdata.csv      nitrousOxidedata.csv
c3f8data.csv   c7f16data.csv                methanedata.csv         sf6data.csv
c4f10data.csv  c8f18data.csv                methylBromidedata.csv
c4f8data.csv   carbonTetraChloridedata.csv  methylChloridedata.csv
c5f12data.csv  co2data.csv                  nf3data.csv
"""

l = l.split()

filenames = []
for i,g in enumerate(l):
    filename = "infile"+str(i)
    vars()[filename] = g
    print(vars()[filename])
    filenames.append(vars()[filename])

#print(filenames)
print(len(filenames))


