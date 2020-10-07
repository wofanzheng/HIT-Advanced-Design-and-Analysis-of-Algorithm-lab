from dataset import *
from Greedy_set_cover import *
from random_rounding import *
import time

'''
print("|X|=|F|=100:")
size=100
X,F=generate_dataset(size)
print("|X|:")
print(X)
print("|F|:")
print(F)
'''

print("|X|=|F|=100:")
size=100
X,F=generate_dataset(size)
time_start=time.time()
C=greedy_set_cover(X,F)
time_end=time.time()
print("贪心法可行解：")
print(len(C))

test=set()
for i in C:
    test=test.union(i)
print(test)

print(C)
print('贪心法消耗时间：',time_end-time_start,'s')

time_start=time.time()
C=lp(X,F)
time_end=time.time()


test=set()
for i in C:
    test=test.union(i)
print(test)


print("线性规划可行解：")
print(len(C))
print(C)
print('线性规划消耗时间：',time_end-time_start,'s')


print("|X|=|F|=1000:")
size=1000
X,F=generate_dataset(size)
time_start=time.time()
C=greedy_set_cover(X,F)
time_end=time.time()
print("贪心法可行解：")
print(len(C))
print(C)
print('贪心法消耗时间：',time_end-time_start,'s')


time_start=time.time()
C=lp(X,F)
time_end=time.time()
print("线性规划可行解：")
print(len(C))
print(C)
print('线性规划消耗时间：',time_end-time_start,'s')


print("|X|=|F|=5000:")
size=5000
X,F=generate_dataset(size)
time_start=time.time()
C=greedy_set_cover(X,F)
time_end=time.time()
print("贪心法可行解：")
print(len(C))
print(C)
print('贪心法消耗时间：',time_end-time_start,'s')

time_start=time.time()
C=lp(X,F)
time_end=time.time()
print("线性规划可行解：")
print(len(C))
print(C)
print('线性规划消耗时间：',time_end-time_start,'s')

