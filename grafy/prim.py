#MST z zadanego wierzcholka
from queue import PriorityQueue
def prim(G,v):
    n=len(G)
    pq=PriorityQueue()
    pq.put((0,v))
    d=[float('inf') for _ in range(n)]
    parent=[None for _ in range(n)]
    vis=[False for _ in range(n)]
    while not pq.empty():
        costam,t=pq.get()
        if not vis[t]:
            vis[t]=True
            for u,w in G[t]:
                if not vis[u]:
                    if d[u]>=w:
                        d[u]=w
                        parent[u]=t
                        pq.put((d[u],u))
    return parent

E=[[(1,1),(2,5),(3,1)],[(0,1),(4,1)],[(3,2),(0,5)],[(2,2),(5,1),(6,1)],[(1,1)],[(3,1)],[(3,1)]]
print(prim(E,0))