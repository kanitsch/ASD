from zad1ktesty import runtests

def roznica( S ):
    #Tutaj proszę wpisać własną implementację
    n=len(S)
    dp=[0 for _ in range(n)]
    maxx=0
    if S[0]=='0':
        dp[0]=1
    for i in range(1,n):
        if S[i]=='0':
            dp[i]=dp[i-1]+1
            maxx=max(maxx,(dp[i]))
        else:
            dp[i]=max(dp[i-1]-1,0)
            #maxx=max(maxx,max(dp[i]))
    if maxx==0:
        return -1
    return maxx

runtests ( roznica )
S='10001011111001010101'
roznica(S)