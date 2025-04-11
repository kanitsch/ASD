from egzP5btesty import runtests 

#akceptowalna?
'''
def DFS_bajojajo(G):
    n=max(max(x) for x in G)+1
    G=lista_sasiedztwa(G,n)
    cnt=[0]
    def DFS_Visit(G,u,cnt):
        nonlocal time
        time+=1
        t[u]=time
        visited[u]=True
        low[u]=time
        for v in G[u]:
            if not visited[v]:
                parent[v]=u
                low[u]=min(low[u],DFS_Visit(G,v,cnt))
            else:
                if not przetw[v] and parent[u]!=v:
                 low[u]=min(low[u],t[v])
        if len(G[u])>1 and low[u]==t[u]:
            cnt[0]+=1
        przetw[u]=True
        return low[u]
    time=0
    n=len(G)
    visited=[False for v in range(n)]
    parent=[None for v in range (n)]
    przetw=[False for v in range(n)]
    low=[float('inf') for _ in range(n)]
    t=[float('inf') for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            DFS_Visit(G,u,cnt)

    return cnt[0]
'''

def DFS_bajojajo(G):
    for i in range(len(G)):
        G[i] = (min(G[i]), max(G[i]))
    n = max(max(x) for x in G) + 1
    G = lista_sasiedztwa(G, n)
    cnt = [0]
    time = 0
    visited = [False] * n
    parent = [-1] * n
    low = [float('inf')] * n
    t = [float('inf')] * n
    articulation_points = set()

    def DFS_Visit(G, u, cnt):
        nonlocal time
        time += 1
        t[u] = low[u] = time
        visited[u] = True
        children = 0

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                DFS_Visit(G, v, cnt)
                low[u] = min(low[u], low[v])

                # If u is not the root and low value of one of its child is greater or equal to t[u]
                if parent[u] != -1 and low[v] >= t[u]:
                    articulation_points.add(u)

                # If u is the root and has more than one child in the DFS tree
                if parent[u] == -1 and children > 1:
                    articulation_points.add(u)

            elif v != parent[u]:  # Update low[u] if v is already visited and is not the parent
                low[u] = min(low[u], t[v])

    for u in range(n):
        if not visited[u]:
            DFS_Visit(G, u, cnt)

    return len(articulation_points)




def DFS(G,s):
    def DFS_Visit(G,u):
        nonlocal time
        time+=1
        visited[u]=True
        for v in G[u]:
            if not visited[v] and v!=s:
                parent[v]=u
                DFS_Visit(G,v)
        time+=1
    time=0
    n=len(G)
    visited=[False for v in range(n)]
    parent=[None for v in range (n)]
    if s!=0:
        DFS_Visit(G,0)
    else:
        DFS_Visit(G,1)
    for u in range(n):
        if not visited[u] and u!=s:
            return 1
    return 0

def lista_sasiedztwa(G,n):
    tab=[[]for _ in range(n)]
    G.sort()
    x=(0,0)
    for (u,v) in G:
        if (u,v)!=x:
            tab[u].append(v) 
            tab[v].append(u)
            x=(u,v)
    return tab

def koleje ( B ):
    #tutaj proszę wpisać własną implementację
    for i in range(len(B)):
        B[i]=(min(B[i]),max(B[i]))
    n=max(max(x) for x in B)+1 
    B=lista_sasiedztwa(B,n)
    #print(B)
    cnt=0
    for u in range(n):
        cnt+=DFS(B,u)
    return cnt
        

runtests ( DFS_bajojajo, all_tests=True )