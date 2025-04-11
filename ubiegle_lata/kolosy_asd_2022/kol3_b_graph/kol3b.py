from kol3btesty import runtests
from queue import PriorityQueue

def dijkstra(n,edgelist,a):
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
    return d

def airports( G, A, s, t ):
    # tu prosze wpisac wlasna implementacje
    d=dijkstra(len(G),G,s) #mlogn
    case1=d[t]
    d_rev=dijkstra(len(G),G,t) #mlogn
    for i in range(len(A)):
        d[i]+=A[i]
        d_rev[i]+=A[i]
    d.sort() #nlogn
    d_rev.sort() #nlogn
    case2=d[0]+d_rev[0]
    return min(case1,case2)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )