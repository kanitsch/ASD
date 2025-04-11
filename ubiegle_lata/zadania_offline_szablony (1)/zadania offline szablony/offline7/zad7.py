from zad7testy import runtests

# cos 7 test nie dziala

def find(G,gate,visited,path,u):
    if len(path)==len(G) and 0 in G[u][gate] and u in G[0][0]:
        return True
    for v in G[u][gate]:
        if not visited[v]:
                visited[v]=True
                path.append(v)
                if u in G[v][0]:
                    if find(G,1,visited,path,v):
                        return True
                if u in G[v][1]:
                    if find(G, 0, visited, path, v):
                        return True
                path.pop()
                visited[v]=False
    return False

def droga1(G):
    n=len(G)
    visited=[False for _ in range(n)]
    visited[0]=True
    path=[0]
    if find(G,1,visited,path,0): return path
    return None

def ispath(G, u, path, n, visited, gate):
        if len(path) == n:
            if 0 in G[u][gate] and u in G[0][1]:
                return True
            return False

        for v in G[u][gate]:
            if not visited[v]:# and not find:
                visited[v] = True
                path.append(v)
                if u in G[v][1]:
                    if ispath(G, v, path, n, visited, 0):
                        return True
                if u in G[v][0]:
                    if ispath(G, v, path, n, visited, 1):
                        return True
                visited[v] = False
                path.pop()
        
        return False

def droga( G ):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    visited = [False] * n
    path = [0]
    visited[0] = True
    res = ispath(G, 0, path, n, visited, 0)
    if res: return path
    else: return None




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga1, all_tests = True )