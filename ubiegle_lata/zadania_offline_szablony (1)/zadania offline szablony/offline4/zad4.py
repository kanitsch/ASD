from zad4testy import runtests

# "Gruby jak armata szczepan błąkał się po kuli ziemskiej"
def select_buildings(T,p):
    n=len(T)
    for i in range(n):
        h,a,b,w=T[i]
        T[i]=(h,a,b,w,i)
    dp=[[0 for _ in range(p+1)] for _ in range(n)]
    poj=[0]*n
    par=[-1 for _ in range(n)]
    T.sort(key=lambda  x: x[2])
    for i in range(n):
        poj[i]=T[i][0]*(T[i][2]-T[i][1])
        j=i-1
        while j>=0:
            if T[j][2]<T[i][1]:
                par[i]=j
                break
            j-=1
    for i in range(p+1):
        if T[0][3]<=i:
            dp[0][i]=poj[0]
    for i in range(1,n):
        for j in range(p+1):
            dp[i][j]=dp[i-1][j]
            if par[i]!=-1 and T[i][3]<=j:
                dp[i][j]=max(dp[i][j],dp[par[i]][j-T[i][3]]+poj[i])
            if par[i]==-1 and T[i][3]<=j:
                dp[i][j]=max(dp[i][j],poj[i])
    i=n-1
    j=p
    res=[]
    while j>0 and i>0:
        if dp[i][j]==dp[i-1][j]:
            i-=1
        elif dp[i][j]==dp[i][j-1]:
            j-=1
        else:
            res.append(T[i][4])
            j-=T[i][3]
            i=par[i]
    if i!=-1 and T[i][3]<=j:
        res.append(T[i][4])

    return sorted(res)

runtests( select_buildings )
