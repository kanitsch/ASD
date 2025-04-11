'''
1. funkcja sprawdzajaca czy: a) graf jest dwudzielny, b) graf ma cykl
2. G nieskierowany, dany macierzowo. podac algorytm sprawdzający czy graf ma cykl dł 4 (lepiej niż O(V^4) )
3. Mówimy że v jest uniwersalnym wyjsciem grafu skierowanego, jesli każdy inny wierzcholek ma krawedz do v, a v nie ma zadnej wychodzacej
algorytm ma sprawdzic czy G dany macierzowo ma uniwersalne wyjście.
4. usuwamy wierzchołki z sieci tak, żeby jej nie rozspójnić
5. graf ma 7 krawędzi o różnych wagach. można poruszać się tylko po rosnacych wagach. czy można przejść z wierzchpka s do t

'''
from collections import deque


def biparted(G):
    n=len(G)
    visited=[0 for _ in range(n)]
    def dfs(v,w):
        visited[v]=w
        for i in G[v]:
            if visited[i]==w:
                return False
            if visited[i]==0:
                res=dfs(i,-1*w)
                if not res:
                    return False
        return True
    return dfs(0,1)

G=[[1],[0,2,4],[1,3],[1,2,4,5],[5],[3,4]]
print(biparted(G))

def cycle(M):
    n=len(M)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    q=deque()
    q.append(0)
    visited[0]=True
    while q:
        s=q.pop()
        for i in range (n):
            if M[s][i]==1:
                if visited[i]==True and parent[s]!=i:
                    return True
                visited[i]=True
                parent[i]=s


def DFS(G):
    def DFS_Visit(G,u):
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                parent[v]=u
                DFS_Visit(G,v)
    n=len(G)
    visited=[False for v in range(n)]
    parent=[None for v in range (n)]
    for u in range(n):
        if not visited[u]:
            DFS_Visit(G,u)
    print(visited, '\n', parent)

def cycle4(M):
    def DFS_Visit(M,u):
        visited[u]=True
        for v in range(n):
            if M[u][v] and not visited[v]:
                parent[v]=u
                if DFS_Visit(M,v):
                    return True
            elif M[u][v]:
                w=u
                cnt=1
                while w and w!=v:
                    w=parent[w]
                    cnt+=1
                    if cnt==4:
                        break
                if cnt==4 and w==v:
                    return True
        return False

    n=len(M)
    visited=[False for v in range(n)]
    parent=[None for v in range (n)]
    for u in range(n):
        if not visited[u]:
            if DFS_Visit(M,u):
                return True
    return False

M=[[0,1,0,0,0,0],[1,0,1,0,1,0],[0,1,0,1,1,0],[0,0,1,0,0,1],[0,1,1,0,0,1],[0,0,0,1,1,0]]
print(cycle4(M))



def uni_wyjscie(G): #moja wersja
    n=len(G)
    for j in range(n):
        flag=True
        for i in range(n):
            if i!=j and (G[i][j]==0 or G[j][i]==1):
                flag=False
                break
        if flag:
            return True
    return False
#G=[[1,1,1,0,1],[1,0,0,0,1],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0]]
#print(uni_wyjscie(G))

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
    return parent



def wypisz(G,s,t):
    path=[]
    p=BFS(G,s)
    v=t
    while v!=None:
        path.append(v)
        v=p[v]
    path.reverse()
    return path

print(wypisz(G,0,3))

def malejace_krawedzie(G,x,y):
        def DFS_Visit(G,u,w):
            visited[u]=True
            if u==y:
                return True
            for v,c in G[u]:
                if last_edge[v]<c<w:
                    last_edge[v]=c
                    if DFS_Visit(G,v,c):
                        return True
            return False
        n=len(G)
        visited=[False for v in range(n)]
        last_edge=[0 for v in range (n)]
        last_edge[x]=float('inf')
        return DFS_Visit(G,x,float('inf'))
G=[[(1,3),(3,4)],[(4,5)],[(1,1),(3,7)],[(0,4)],[(2,6)]]
print(malejace_krawedzie(G,2,0))


