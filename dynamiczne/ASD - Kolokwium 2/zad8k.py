from zad8ktesty import runtests 

def uzup(s,t,dp,a,b):
    if dp[a][b]!=float('inf'):
        return dp[a][b]
    if t[a]!=s[b]:
        dp[a][b]=min(uzup(s,t,dp,a-1,b),uzup(s,t,dp,a-1,b-1),uzup(s,t,dp,a,b-1))+1
        return dp[a][b]
    dp[a][b]=uzup(s,t,dp,a-1,b-1)
    return dp[a][b]

def napraw ( s, t ):
    n=len(s)
    m=len(t)
    dp=[[float('inf') for _ in range(n)] for _ in range(m)]
    if s[0]==t[0]:
        dp[0][0]=0
    else:
        dp[0][0]=1
    for i in range(1,n):
        if s[i]==t[0]:
            dp[0][i]=i
        else:
            dp[0][i]=dp[0][i-1]+1
    for i in range(1,m):
        if t[i]==s[0]:
            dp[i][0]=i
        else:
            dp[i][0]=dp[i-1][0]+1
        
    return uzup(s,t,dp,m-1,n-1)

runtests ( napraw )