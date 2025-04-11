from zad3ktesty import runtests

def ksuma( T, k ):
    #Tutaj proszę wpisać własną implementację
    n=len(T)
    dp=[[float('inf'),float('inf')] for _ in range(n)]
    for i in range(n):
        for j in range(i,min(i+k,n)):
            if i>=k:
                dp[j][0]=min(dp[j][0],dp[i-1][0]+T[i])
                dp[j][1]=dp[i-1][0]+T[i]
            else:
                dp[j][0]=min(dp[j][0],T[i])
                dp[j][1]=T[i]
    return dp[-1][0]
    
runtests ( ksuma )