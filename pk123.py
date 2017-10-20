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
    #print(list1[i])
    #print(k)
    #print("\n")
    objects=list(objects)
    objects.insert(i,list1[i])
    objects=tuple(objects)
    y.append(k)
#y_pos=np.arange(len(objects))
#barchart=mt.bar(y_pos,y,align='center',width=0.2,label='yo')
#for i in range(0,15):
#    if i%2==0:
#        barchart[i].set_color('r')
#mt.xticks(y_pos,objects,size=6)
#mt.legend()
#mt.rc('xtick',labelsize=10)
#mt.show()
fig_size=mt.rcParams["figure.figsize"]  
fig_size[1]=50 
fig_size[0]=50 
mt.rcParams["figure.figsize"]=fig_size 
mt.xlim([-2,450])
j=0
mt.ylabel('Co level(mean)') 
for i in range(0,450,2):
     mt.bar(i,k[j],width=1.5,label=list1[j])
     j=j+1
mt.xticks(np.arange(0,450,2),list1,size=4,rotation='vertical')
#freq_ser=pd.Series.from_array(k)
#k1=freq_ser.plot('bar',width=5,color='r')
#k1.set_xticklabels(objects,size=5)
#rects=k1.patches
#for rect,lis in zip(rects,list1):
#    height=rect.get_height()
#    k1.text(rect.get_x()+rect.get_width()/2,height+3,lis,size=5,verticalalignment='center',horizontalalignment='left',rotation='vertical')
#mt.xticks(np.arange(225),objects,size=3,rotation='vertical')
mt.legend(loc='upper right',prop={'size':5},labelspacing=0.2)
#mt.bar(np.arange(len(objects)),k,width=3)
#mt.xlim([0,300])
#mt.xticks(np.arange(len(list1)),objects,size=3)
mt.show()

       






