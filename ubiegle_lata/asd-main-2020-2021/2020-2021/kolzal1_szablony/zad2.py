from zad2testy import runtests

def DFS(G):
    def DFS_Visit(G,u,i):
        visited[u]=True
        for v in range(n):
            if G[u][v] and v!=i and not visited[v]:
                DFS_Visit(G,v,i)
    n=len(G)
    maxx=1
    sol=None
    for i in range(n):
        cnt=0
        visited = [False for v in range(n)]
        for u in range(n):
            if u!=i and not visited[u]:
                cnt+=1
                DFS_Visit(G,u,i)
        if cnt>maxx:
            maxx=cnt
            sol=i
    return sol if maxx>1 else None
def breaking(G):
    # tu prosze wpisac wlasna implementacje
    return DFS(G)


runtests( breaking )