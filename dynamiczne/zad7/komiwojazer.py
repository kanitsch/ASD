from math import sqrt

def komiwojazer_bitoniczny(L):
    D=odl(L)
    n = len(D)
    F = [[float('inf') for _ in range(n)] for _ in range(n)]
    F[0][1]=D[0][1]

    def tspf(i, j):
        if F[i][j] != float('inf'):
            return F[i][j]
        if i == j - 1:
            best = float('inf')
            for k in range(j - 1):
                best = min(best, tspf(k, j - 1) + D[k][j])
            F[j - 1][j] = best
        else:
            F[i][j] = tspf(i, j - 1) + D[j - 1][j]
        return F[i][j]

    minn = float('inf')
    for i in range(n-1):
        minn = min(minn, tspf(i, n - 1) + D[i][n - 1])
    return minn


def odl(L):
    L.sort()
    n=len(L)
    D=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            D[i][j]=sqrt((L[j][0]-L[i][0])**2+(L[j][1]-L[i][1])**2)
            D[j][i]=sqrt((L[j][0]-L[i][0])**2+(L[j][1]-L[i][1])**2)
    return D

L=[(0,6),(1,0),(2,3),(5,4),(6,1),(7,5),(8,2)]
print(komiwojazer_bitoniczny(L))