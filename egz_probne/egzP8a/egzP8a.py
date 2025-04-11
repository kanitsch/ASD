from egzP8atesty import runtests


def meine_reklamy(T,S,o):
    n=len(T)
    for i in range(n):
        T[i]=(T[i][0],T[i][1],S[i])
    maxx=0
    T.sort()
    for i in range(n):
        zysk=T[i][2]
        for j in range(i+1,n):
            if T[i][1]>=T[j][0]:
                continue
            zysk=max(zysk,T[i][2]+T[j][2])
        maxx=max(maxx,zysk)
    return maxx 

def find(tab,l,p,x):
    mid=(l+p)//2
    if l==p:
        return p
    if tab[mid][0]<=x:
        if mid+1<p and tab[mid+1][0]>x:
            return mid+1
        return find(tab,mid+1,p,x)
    if mid-1>=0 and tab[mid-1][0]<x:
        return mid
    return find(tab,l,mid,x)    
    

def reklamy_wz(T,S,o):
    n=len(T)
    for i in range(n):
        T[i]=(T[i][0],T[i][1],S[i]) 
    T.sort()
    dp=[0 for _ in range(n)]
    dp[n-1]=T[n-1][2]
    maxx=0
    for i in range(n-2,-1,-1):
        dp[i]=max(dp[i+1],T[i][2])
        maxx=max(maxx,dp[i])
    for i in range(n):
        j=find(T,0,n,T[i][1])
        if j<n:
            maxx=max(T[i][2]+dp[j],maxx)
    return maxx

runtests ( reklamy_wz, all_tests=True )