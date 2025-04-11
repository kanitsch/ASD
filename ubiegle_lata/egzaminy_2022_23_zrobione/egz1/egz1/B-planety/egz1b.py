from egz1btesty import runtests

def planets( D, C, T, E ):
    n=len(D)
    A=[[float('inf') for _ in range(E+1)] for _ in range(n)]
    for j in range(E+1):
        A[0][j]=j*C[0]
    if T[0][0]>0:
        A[T[0][0]][0]=T[0][1]
    for i in range(1,n):
        dist=D[i]-D[i-1]
        for j in range(dist,E+1):
            A[i][j-dist]=min(A[i][j-dist],A[i-1][j])
        for j in range(1, E+1):
            A[i][j]=min(A[i][j],A[i][j-1]+C[i])
        if T[i][0]>i:
            A[T[i][0]][0]=min(A[T[i][0]][0],A[i][0]+T[i][1])
    return A[n-1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
