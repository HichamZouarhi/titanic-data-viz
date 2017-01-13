#!/usr/bin/env python
import numpy as np
import pandas as pd

data = pd.read_csv('titanic-data.csv')

dead =pd.Series([])
status =pd.Series([])
count = pd.Series(1,np.arange(len(data)))
data['count']=count

for index,row in data.iterrows():
	dead[index]=(0 if row['Survived']==1 else 1)
	status[index]=('Survived' if row['Survived']==1 else 'Died')

data['Status']=status

data1 = data.groupby([pd.cut(data["Age"], np.arange(0, 80, 10)),'Status'])['count'].sum()

print data1
data1.to_csv('data-by-age.csv',header=True)
	
data['Died']=dead

data.to_csv('titanic-data.csv',header=True, index=False)
