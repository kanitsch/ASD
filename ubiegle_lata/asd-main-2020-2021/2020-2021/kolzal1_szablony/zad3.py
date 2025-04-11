from zad3testy import runtests



def iamlate(T, V, q, l):
    """tu prosze wpisac wlasna implementacje"""
    if T[-1]!=l:
        T.append(l)
        V.append(0)
    n=len(T)
    dp=[[float('inf') for _ in range(q+1)] for _ in range(n)]
    dp[0][0]=0
    for i in range(1,min(q,V[0])+1):
        dp[0][i]=1
    for i in range(1,n):
        for j in range(q+1):
            if T[i]-T[i-1]+j<=q:
                dp[i][j]=min(dp[i-1][T[i]-T[i-1]+j],dp[i][j])
                for k in range(j+1,min(j+V[i]+1,q+1)):
                    dp[i][k]=min(dp[i][k],dp[i][j]+1)
    if min(dp[-1])==float('inf'):
        return []
    mini=float('inf')
    sol=[]
    for i in range(q+1):
        if dp[-1][i]<mini:
            mini=dp[-1][i]
            ind=i
    for i in range(n-1,0,-1):
        if dp[i][max(0,ind-V[i])]<dp[i][ind]:
            sol.append(i)
            ind=max(0,ind-V[i])
        ind+=T[i]-T[i-1]
        
    sol.append(0)
    sol.reverse()

            
    return sol

def iamlate_better(T,V,q,l):
    if T[-1]!=l:
        T.append(l)
        V.append(0)
    n=len(T)
    dp=[[float('inf') for _ in range(q+1)] for _ in range(n)]
    parent=[[[-1,-1] for _ in range(q+1)] for _ in range(n)]
    dp[0][0]=0
    dp[0][min(q,V[0])]=1
    for i in range(n):
        for j in range(q+1):
            if dp[i][j]!=float('inf'):
                if i+1<n and T[i+1]-T[i]<=j:
                    newfuel=min(q,j-T[i+1]+T[i]+V[i+1])
                    if dp[i+1][newfuel]>dp[i][j]+1:
                        dp[i+1][newfuel]=dp[i][j]+1
                        parent[i+1][newfuel]=[i,j]
    if min(dp[-1])==float('inf'):
        return []
    fuel=0
    mini=float('inf')
    for i in range(q+1):
        if dp[-1][i]<mini:
            mini=dp[-1][i]
            fuel=i
    i=n-1
    sol=[]
    while parent[i][fuel]!=[-1,-1]:
        i,fuel=parent[i][fuel]
        sol.append(i)
    sol.reverse()
    return sol
    
                    
    


runtests( iamlate )