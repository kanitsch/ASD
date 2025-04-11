from zad5testy import runtests
from queue import PriorityQueue

def plan(T):
    # tu prosze wpisac wlasna implementacje
    n=len(T)
    S=T.copy()
    d=[0 for _ in range(n)]
    d[0]=1
    S[0]=0
    pq=PriorityQueue()
    zapas=T[0]
    i=0
    while i<n:
        while i<n-1 and zapas:
            i+=1
            if S[i]>0:
                pq.put((-S[i],i))
            zapas-=1
        if i==n-1:
            break
        maxspan,ind=pq.get()
        maxspan*=-1
        S[ind]=0
        zapas=maxspan
    res=[]
    for i in range(n):
        if T[i]!=S[i]:
            res.append(i)

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )