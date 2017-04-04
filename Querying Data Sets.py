#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 2017
@author: AMJ
"""
#***********************************************************************************
# Simple min and max queries in python for a small data set of world city visits. 
#
#***********************************************************************************
#%%
import pandas as pd
import os
folderName='Data'
fileName='cities.xlsx'
fileExcel=os.path.join(folderName,fileName)
citystats=pd.read_excel(fileExcel)
citystats
#%%

# What was the most visited city in 2015?
citystats[citystats.visits2015==max(citystats.visits2015)].city

#%%
# What was the least visited city in Asia in 2013?
AsiaOnly=citystats[(citystats.region=='Asia')]
AsiaOnly       
AsiaOnly.reset_index()   
AsiaOnly.reset_index(drop=True)   
AsiaOnly[AsiaOnly.visits2013==min(AsiaOnly.visits2013)].city

#%%
# What are the three least visited cities in Asia in 2015?    
toSort=["visits2015"]
Order=[True]
Rank2015=AsiaOnly.sort_values(by=toSort,ascending=Order,).reset_index()
Rank2015.head(3).city
#%%
# What are the most and least visited cities in Asia in 2013?
toSort=["visits2013"]
Order=[True]
Rank2013=AsiaOnly.sort_values(by=toSort,ascending=Order,).reset_index()
Rank2013
Rank2013.iloc[[0,-2],:].city
#%%

