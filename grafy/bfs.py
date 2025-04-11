from queue import Queue
from collections import deque

def BFS(G,s): #uznaje ze G jest lista sasiedztwa
    Q=Queue()
    n=len(G)
    d=[-1 for v in range(n)]
    visited=[False for v in range(n)]
    parent=[None for v in range (n)]
    visited[s]=True
    d[s]=0
    Q.put(s)
    while not Q.empty():
        u=Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v]=True
                d[v]=d[u]+1
                parent[v]=u
                Q.put(v)
    print(d,parent,visited,sep='\n')       #dlaczego nie działa???   już działa!!! 
    
G=[[1],[4,2,0],[3,2],[4,1],[2]]   
BFS(G,2)

d=deque()
d.append('papu')
d.append('aaa')
x=d.popleft()
print(x)
