from zad1testy import runtests
from copy import deepcopy
from queue import Queue

def floyd_warshall_marshall(M):
    n=len(M)
    S=deepcopy(M)
    for i in range(n):
        S[i][i]=0
    for i in range(n):
        for j in range(n):
            if i!=j and S[i][j]==0:
                S[i][j]=float('inf')
    for k in range(n):
        for x in range(n):
            for y in range(n):
                S[x][y]=min(S[x][y], S[x][k]+S[k][y])
    return S


def keep_distance(M, x, y, d):
    # tu prosze wpisac wlasna implementacje
    s,t=x,y
    n=len(M)
    S=floyd_warshall_marshall(M)
    vis=[[False for _ in range(n)]for _ in range(n)]
    parent=[[None for _ in range(n)] for _ in range(n)]
    q=Queue()
    q.put((x,y))
    while not q.empty():
        x,y=q.get()
        vis[x][y]=True
        if x==t and y==s:
            break
        for i in range(n):
            if M[x][i] and S[i][y]>=d and not vis[i][y]:
                parent[i][y]=(x,y)
                q.put((i,y))
            if M[i][y] and S[x][i]>=d and not vis[x][i]:
                parent[x][i]=(x,y)
                q.put((x,i))
            if M[i][x]:
                for j in range(n):
                    if M[j][y] and S[i][j]>=d and not vis[i][j] and (i!=y or j!=x):
                        parent[i][j]=(x,y)
                        q.put((i,j))
    path=[]
    x,y=t,s
    while x!=s or y!=t:
        path.append((x,y))
        x,y=parent[x][y]
    path.append((x,y))
    path.reverse()
    return path


runtests( keep_distance )