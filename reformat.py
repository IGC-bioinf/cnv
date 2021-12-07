#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:19:57 2021

@author: roma
"""
import pandas as pd
df = pd.read_csv('/home/roma/cnv/for_common_count.csv', sep='\t', header=None)
fl = []
for i in range(len(df)):
    if ',' in df[1][i]:
        for k in range(len(df[1][i].split(','))):
                       pat=str(df[0][i]) + '\t' + str(df[1][i].split(',')[k]) + '\t' + str(df[2][i])
                       fl.append(pat)
    else:
        pat= str(df[0][i])+'\t'+str(df[1][i])+'\t'+ str(df[2][i])
        fl.append(pat)
print (fl)