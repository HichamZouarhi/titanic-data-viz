#!/usr/bin/env python
import json
import pandas as pd
import os

data = pd.read_csv('titanic-data.csv')

dead =pd.Series([])

for index,row in data.iterrows():
	print index
	dead[index]=(0 if row['Survived']==1 else 1)
	
data['Died']=dead
#print data['Died']

data.to_csv('titanic-data.csv',header=True, index=False)

#print data.describe()