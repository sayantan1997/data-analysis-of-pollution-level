import numpy as np
import pandas as pd
import matplotlib.pyplot as mt
data=pd.read_csv('2-2017(PETROL).csv');
print(data.describe())
temp1=data['Vehicle_Model'].value_counts(ascending=True)
print(temp1)
poll=input("enter choice of pollutant: 1.Co 2.HC 3.CO2 4.O2")
time=np.array(data['Vehicle_Model'][1:])
time2=np.array(data[poll][1:])
dict1={}
mt.title('january 2017')
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
objects=()
y=[]
k=[]
print(len(list1))
for i in range(0,len(list1)):
    temp2=np.array(dict1[list1[i]])
    k.append(temp2.mean())
    objects=list(objects)
    objects.insert(i,list1[i])
    objects=tuple(objects)
    y.append(k)
fig_size=mt.rcParams["figure.figsize"]  
fig_size[1]=50 
fig_size[0]=50 
mt.rcParams["figure.figsize"]=fig_size 
mt.xlim([-2,len(list1)*2])
j=0
<<<<<<< HEAD
p=0.5
count=0
maxi=max(k)
mini=min(k)
avg=(maxi+mini)/2
print(avg)
print(k[0])
print(k[1])
mt.ylabel(poll+'(mean)') 
for i in range(0,len(list1)*2,2):
     mt.bar(i,k[j],width=1,label=list1[j])
     if(k[j]>100 and count<1):
        p=p*1000
        count=count+1
     if(k[j]<avg):
        mt.text(i,k[j]+(avg/5),list1[j],verticalalignment='top',rotation='vertical',size=4,color='brown',style='oblique',weight='bold')
=======
i1=[]
mt.ylabel('Co level(mean)') 
for i in range(0,len(list1)*2,2):
     mt.bar(i,k[j],width=2,label=list1[j])
     if(k[j]<=2):
         mt.text(i,k[j]+1.5,list1[j],verticalalignment='top',horizontalalignment='center',rotation='vertical',size=4,color='green',style='oblique',weight='bold')
>>>>>>> f6f7d486b94d9afe24f8de5834d0cd10d7f66645
     else:
        mt.text(i,k[j]+(k[j]/10),list1[j],verticalalignment='top',rotation='vertical',size=4,color='green',style='oblique',weight='bold')
     j=j+1
k3=mt.subplot()
k4=k3.get_ylim()
print(k4[0])
#j=0
#for i in range(0,len(list1)*2,2):
#     mt.text(i,k[j]+k4[1]//10,list1[j],verticalalignment='top',horizontalalignment='center',rotation='vertical',size=4,color='green',style='oblique',weight='bold')
#     j=j+1
mt.xticks(np.arange(0,len(list1)*2,2),list1,size=3,rotation='vertical',weight='bold')
mt.show()

       






