from zad11ktesty import runtests

def rek(T,i=0,suma=0):
    if i==len(T):
        return suma
    return min(abs(rek(T,i+1,suma+T[i])),abs(rek(T,i+1,suma-T[i])))


def kontenerowiec(T):
    #Tutaj proszę wpisać własną implementację
    s=sum(T)
    m=s//2
    n=len(T)
    dp=[[0 for _ in range(m+1)] for _ in range(n)]
    dp[0][T[0]]=1
    dp[0][0]=1
    for i in range(1,n):
        for x in range(m+1):
            if x>=T[i]:
                dp[i][x]=max(dp[i-1][x],dp[i-1][x-T[i]])
            else:
                dp[i][x]=dp[i-1][x]
    for i in range(m,-1,-1):
        if dp[-1][i]==1:
            return s-2*i


runtests ( kontenerowiec )
    