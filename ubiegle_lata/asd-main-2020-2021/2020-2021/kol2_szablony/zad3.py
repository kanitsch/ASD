from zad3testy import runtests
from queue import PriorityQueue

def ropa(T,y,x):
    r=T[y][x]
    T[y][x]=0
    if x+1<len(T[0]) and T[y][x+1]!=0:
        r+=ropa(T,y,x+1)
    if x-1>=0 and T[y][x-1]!=0:
        r+=ropa(T,y,x-1)
    if y+1<len(T) and T[y+1][x]!=0:
        r+=ropa(T,y+1,x)
    if y-1>=0 and T[y-1][x]!=0:
        r+=ropa(T,y-1,x)
    return r


def plan(T):
    # tu prosze wpisac wlasna implementacje
    n=len(T)
    for i in range(len(T[0])):
        if T[0][i]!=0:
            T[0][i]=ropa(T,0,i)
    q=PriorityQueue()
    bak=T[0][0]
    result=[0]
    j=0
    while j<n:
        for i in range(j+1,min(j+bak+1,n)):
            if T[0][i]!=0:
                q.put((-T[0][i],i))
        if i==n-1:
            return sorted(result)
        bak,idx=q.get()
        bak*=-1
        result.append(idx)
        j=i
    return None


runtests(plan)
