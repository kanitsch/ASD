from zad2testy import runtests

from queue import Queue

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
    return d, parent

def enlarge(G, s, t):
    # tu prosze wpisac wlasna implementacje
    d,parent=BFS(G,s)
    length=d[t]
    i=t
    while parent[i]!=None:
        G[parent[i]].remove(i)
        G[i].remove(parent[i])
        d,p=BFS(G,s)
        l2=d[t]
        if l2>length:
            return (parent[i],i)
        G[i].append(parent[i])
        G[parent[i]].append(i)
        i=parent[i]
    return None

runtests( enlarge ) 
