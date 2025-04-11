from kol2atesty import runtests

def uzup(dp,i,os,tab):
    n=len(dp)
    if i==n-1:
        dp[i][os]=0
        return 0
    if dp[i][os]<float('inf'):
        return dp[i][os]
    if os==0:
        res=float('inf')
        for j in range(i+1,min(i+4,n)):
            res=min(uzup(dp,j,1,tab),res)
        dp[i][0]=res
        return res
    if os==1:
        res = float('inf')
        ctrl=0
        for j in range(i + 1, min(i + 4, n)):
            ctrl += tab[j][0]
            res = min(uzup(dp, j, 0,tab)+ctrl, res)
        dp[i][1] = res
        return res


def drivers( P, B ):
    # tu prosze wpisac wlasna implementacje
    n=len(P)
    inf=float('inf')
    for i in range(n):
        P[i]=(P[i][0],P[i][1],i)
    P.sort()
    prz=[]
    ctrl=0
    for point in P:
        if point[0]>=B:
            break
        if point[1]:
            prz.append((ctrl, point[2]))
            ctrl=0
        else:
            ctrl+=1
    prz.append((ctrl,n))
    prz.insert(0,(0,0))
    m=len(prz)
    dp=[[inf,inf] for _ in range(m)]
    uzup(dp,1,0,prz)
    uzup(dp,0,0,prz)
    print(dp)
    res=[]
    os=0
    point=0
    cnt=0
    for i in range(1,m-1):
        cnt+=prz[i][0]
        if os==0 and dp[i][1]==dp[point][0]:
            res.append(prz[i][1])
            os=1
            point=i
            cnt=0
        elif os==1 and dp[point][1]==dp[i][0]+cnt:
            res.append(prz[i][1])
            os=0
            point=i
            cnt=0
    return res

# i znowu marian ze schodow spadl i calkiem mu sie pozmienial swiat


runtests( drivers, all_tests = True)

