
def greedy_set_cover(X,F):
    U=X
    C=[]
    while len(U)!=0:
        maxsetsi=-1
        maxset=set()
        for s in F:
            if len(U.intersection(s))>maxsetsi:
                maxset=s
                maxsetsi=len(U.intersection(s))
        U=U.difference(maxset)
        C.append(maxset)
        #print(U)
    return C

