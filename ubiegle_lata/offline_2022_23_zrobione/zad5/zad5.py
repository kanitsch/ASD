from zad5testy import runtests

from queue import PriorityQueue

'''to samo było u nas jako offline 5'''

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    def relax(u,v):
        if d[v[0]]>d[u]+v[1]:
            d[v[0]]=d[u]+v[1]
            pq.put((d[v[0]],v[0]))
    edgelist=[[]for _ in range(n)]
    for el in E:
        edgelist[el[0]].append([el[1],el[2]])
        edgelist[el[1]].append([el[0],el[2]])
    for i in range(len(S)):
        for j in range (i+1,len(S)):
            edgelist[S[i]].append([S[j],0])
            edgelist[S[j]].append([S[i],0])
    visited=[False for _ in range(n)]
    pq=PriorityQueue()
    d=[float("inf") for _ in range(n)]
    d[a]=0
    pq.put((d[a],a))
    u=a
    while u!=b:
        for v in edgelist[u]:
            relax(u,v)
        visited[u]=True
        while visited[u]:
            if pq.empty(): return None
            u=pq.get()[1]
    return d[b]
        
       

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = False )