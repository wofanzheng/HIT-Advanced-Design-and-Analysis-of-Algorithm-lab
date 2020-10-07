import BruteForceCH 
import GrahamScanCH 
import DivideCH
import time

'''
for i in range(1000,30000,1000):
    data=[]
    data_o=[]
    data,data_o=BruteForceCH.generate_data(i,data,data_o)
    time_start=time.time()
    BruteForceCH.BruteForceCH(i,data,data_o)
    time_end=time.time()
    print(time_end-time_start)
'''

#'''
for i in range(1000,30000,1000):
    data=[]
    data=GrahamScanCH.generate_data(i,data)
    time_start=time.time()
    GrahamScanCH.GrahamScanCH(i,data)
    time_end=time.time()
    print(time_end-time_start)
#'''



for i in range(1000,30000,1000):
    data=[]
    data=DivideCH.generate_data(i,data)
    time_start=time.time()
    DivideCH.DivideCH(i,data)
    time_end=time.time()
    print(time_end-time_start)
