import numpy as np
import pandas as pd
import matplotlib.pyplot as mt
data=pd.read_csv('mod2017.csv');
print(data.describe())
temp1=data['Vehicle_Model'].value_counts(ascending=True)
print(temp1)
time=np.array(data['Vehicle_Model'][1:])
time2=np.array(data['Co'][1:])
dict1={}
for i in range(0,len(time)):
    if(time[i] not in dict1.keys()):
        key=time[i]
        value=time2[i]
        dict1.setdefault(key,[]).append(value)
        for j in range(i+1,len(time)):
            if(time[i]==time[j]):
                 value=time2[j]
                 dict1.setdefault(key,[]).append(value)
list1=[]
list1=dict1.keys()
#mt.subplots(len(list1),len(list1))
#mt.plot(dict1[list1[120]])
#mt.show()
for i in range(0,15):
    mt.ylabel('CO level')
    mt.xlabel(list1[i])
    if(len(dict1[list1[i]])==1):
        #mt.subplot(2,2,i+1)
        mt.plot(dict1[list1[i]],'ro')
        mt.show()
    else:
        #mt.subplot(2,2,i+1)
        mt.plot(dict1[list1[i]])
        mt.show()

       






