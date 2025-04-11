from egzP7atesty import runtests 
from math import inf

def obojetne(T):
    cnt=0
    for krotka in T:
        if krotka==(None,None,None):
            cnt+=1
    return cnt
 
def DFS(G,s,t,parent):
    def DFS_Visit(G,u,visited,parent):
        visited[u]=True
        for v in range(n):
            if not visited[v] and G[u][v]!=0:
                parent[v]=u
                DFS_Visit(G,v,visited,parent)
    n=len(G)
    visited=[False for v in range(n)]
    DFS_Visit(G,s,visited,parent)
    return visited[t]      

def ford_fulk(G,s,t):
    parent=[None for _ in range(len(G))]
    max_flow=0
    while DFS(G,s,t,parent):
        curr_flow=inf
        curr=t
        while curr!=s:
            curr_flow=min(curr_flow,G[parent[curr]][curr])
            curr=parent[curr]
        max_flow+=curr_flow
        v=t
        while v!=s:
            u=parent[v]
            G[u][v]-=curr_flow
            G[v][u]+=curr_flow
            v=parent[v]
    return max_flow
            
              

def akademik( T ):
    #Tutaj proszę wpisać własną implementację
    s=len(T)*2
    t=s+1
    n=t+1
    n1=len(T)
    G=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n1):
        for j in range(3):
            if T[i][j]:
                G[i][n1+T[i][j]]=1
    for i in range(n1):
        G[s][i]=1
        G[n1+i][t]=1

    return n1-obojetne(T)-ford_fulk(G,s,t)

runtests ( akademik )



