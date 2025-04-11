from zad3testy import runtests
from zad3EK    import edmonds_karp


def floyd_warshall_marshall(S):
    n=len(S)
    for i in range(n):
        for j in range(n):
            if i!=j and S[i][j]==0:
                S[i][j]=float('inf')
    for k in range(n):
        for x in range(n):
            for y in range(n):
                S[x][y]=min(S[x][y], S[x][k]+S[k][y])
    return S

def BlueAndGreen(T, K, D):
    # tu prosze wpisac wlasna implementacje
    S=floyd_warshall_marshall(T)
    n=len(T)
    newT=[[0 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            if K[i]=='B' and K[j]=='G' and S[i][j]>=D:
                newT[i][j]=1
                newT[n][i]=1
                newT[j][n+1]=1
    return edmonds_karp(newT,n,n+1)

runtests( BlueAndGreen ) 
