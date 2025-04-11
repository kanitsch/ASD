from kol3atesty import runtests

from queue import PriorityQueue

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    edgelist=[[]for _ in range(n)]
    for el in E:
        edgelist[el[0]].append([el[1],el[2]])
        edgelist[el[1]].append([el[0],el[2]])
    for i in range(len(S)):
        for j in range (i+1,len(S)):
            edgelist[S[i]].append([S[j],0])
            edgelist[S[j]].append([S[i],0])
    pq=PriorityQueue()
    d=[float("inf") for _ in range(n)]
    d[a]=0
    pq.put((d[a],a))
    u=a
    while not pq.empty():
        _,u=pq.get()
        for v in edgelist[u]:
            if d[v[0]]>d[u]+v[1]:
                d[v[0]]=d[u]+v[1]
                pq.put((d[v[0]],v[0]))
    if d[b]==float('inf'):
        return None
    return d[b]

def dijkstra(G,a):
    n=len(G)
    pq=PriorityQueue()
    d=[float("inf") for _ in range(n)]
    d[a]=0
    pq.put((d[a],a))
    while not pq.empty():
        _,u=pq.get()
        for v in G[u]:
            if d[v[0]]>d[u]+v[1]:
                d[v[0]]=d[u]+v[1]
                pq.put((d[v[0]],v[0]))
    return d   
   
def spacetravel2(n,E,S,a,b):      
    edgelist=[[]for _ in range(n)]
    for el in E:
        edgelist[el[0]].append([el[1],el[2]])
        edgelist[el[1]].append([el[0],el[2]])      
    d1=dijkstra(edgelist,a)
    d2=dijkstra(edgelist,b)
    min1=float('inf')
    min2=float('inf')
    for i in S:
        min1=min(min1,d1[i])
        min2=min(min2,d2[i])
    res=min(d1[b],min1+min2)
    if res==float('inf'):
        return None
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel2, all_tests = True )