from zad1testy import runtests
from math import inf

def przeciecie(kw1,kw2):
    x1=min(max(kw1[0],kw2[0]),kw1[2],kw2[2])
    y1=min(max(kw1[1],kw2[1]),kw1[3],kw2[3])
    x2=min(kw1[2],kw2[2])
    y2=min(kw1[3],kw2[3])
    return (x1,y1,x2,y2,(x2-x1)*(y2-y1))
    


def rect(D):
    """tu prosze wpisac wlasna implementacje"""
    D.insert(0,(-inf,-inf,inf,inf,inf))
    D.append((-inf,-inf,inf,inf,inf))
    n=len(D)
    t1=[()  for _ in range(n)]
    t2=[()  for _ in range(n)]
    t1=D.copy()
    t2=D.copy()
    for i in range(1,n):
        t1[i]=przeciecie(t1[i-1],t1[i])
    for i in range(n-2,-1,-1):
        t2[i]=przeciecie(t2[i+1],t2[i]) 
    best=0
    sol=0
    for i in range(1,n-1):
        res=przeciecie(t1[i-1],t2[i+1])[4]   
        if res>best:
            best=res 
            sol=i  
    return sol-1

    
runtests( rect )


