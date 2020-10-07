import random

def generate_dataset(size):
    X=set()
    F=[]
    for i in range(size):
        X.add(i)
    si = set(random.sample(X,20))
    F.append(si)
    sum_set=set()
    sum_set=sum_set.union(si)
    while True:
        n=random.randint(0,20)
        x=random.randint(0,n)
        si=set()
        dif=X.difference(sum_set)
        if len(dif)<20:
            si=dif
            F.append(si) 
            sum_set=sum_set.union(si)
            break
        else:
            si=si.union(set(random.sample(sum_set,n-x)),set(random.sample(dif,x)))
            F.append(si)
            sum_set=sum_set.union(si)
    gap=size-len(F)
    for i in range(gap):
        n=random.randint(0,20)
        F.append(set(random.sample(X,n)))
    return X,F


    
