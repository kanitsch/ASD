from zad4ktesty import runtests

def uzup(dp,T,i,j):
    if dp[i][j]<float('inf'):
        return dp[i][j]
    dp[i][j]=min(uzup(dp,T,i-1,j),uzup(dp,T,i,j-1))+T[i][j]
    return dp[i][j]

def falisz ( T ):
    #Tutaj proszę wpisać własną implementację
    n=len(T)
    dp=[[float('inf') for _ in range(n)] for _ in range(n)]
    dp[0][0]=0
    for i in range(1,n):
        dp[0][i]=dp[0][i-1]+T[0][i]
        dp[i][0]=dp[i-1][0]+T[i][0]
    
    return uzup(dp,T,n-1,n-1)

runtests ( falisz )
