#-*- coding:utf-8 -*-
from pulp import *


def lp(X,F):
    size=len(X)
    Sets=[]
    C=[]
    for i in range(size):
        Sets.append("S"+str(i)) 
    #创建问题实例，求最小极值
    prob = LpProblem("Set covering problem", LpMinimize)
    #构建Lp变量字典,下界是0
    Sets_vars = LpVariable.dicts("",Sets,0)
    #添加目标方程
    prob += lpSum([1*Sets_vars[i] for i in Sets])
    maxf=-1
    for i in range(size):
        f=0
        #记录每个点分别包含在哪些集合中，构造约束函数
        Point_contain={}
        for j in range(size):
            if i in F[j]:
                key="S"+str(j)
                Point_contain[key]=1
                f=f+1
            else:
                key="S"+str(j)
                Point_contain[key]=0
        if f>maxf:
            maxf=f
        #添加约束方程
        prob += lpSum([Point_contain[i] * Sets_vars[i] for i in Sets]) >= 1.0
        #求解
    prob.solve()
    #查看解的状态
    #print("Status:", LpStatus[prob.status])
    #查看解
    #for v in prob.variables():
    #    print(v.name, "=", v.varValue)
    #for i in Sets:
    #    print(Sets_vars[i],"=",Sets_vars[i].value())

    j=0
    for i in Sets:
        if Sets_vars[i].value()>=1.0/maxf:
            C.append(F[j])
        j=j+1
    print("f:",maxf)
    return C     


