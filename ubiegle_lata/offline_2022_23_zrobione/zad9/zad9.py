from zad9testy import runtests

def min_cost( O, C, T, L ):
    n=len(O)
    A=[(O[i],C[i]) for i in range(n)]
    A.sort()
    O[0]=C[0]=0
    for i in range(n-1):
        O[i+1]=A[i][0]
        C[i+1]=A[i][1]
    O.append(A[n-1][0])
    O.append(L)
    C.append(A[n-1][1])
    C.append(0)
    DP=[[float('inf') for _ in range(n+2)] for _ in range(2)]
    DP[0][0]=0
    h=k=0
    while h<=n+2:
        i=j=h+1
        l=k+1
        min_ind_T1=h+1
        min_ind_T2=k+1
        while i<n+2 and O[i]-O[h]<=T:
            DP[0][i]=min(DP[0][i],DP[0][h]+C[i])
            if DP[0][i]<=DP[0][min_ind_T1]: min_ind_T1=i
            i+=1
        while j<n+2 and O[j]-O[h]<=2*T:
            DP[1][j]=min(DP[1][j],DP[0][h]+C[j])
            j+=1
        while l<n+2 and O[l]-O[k]<=T:
            DP[1][l]=min(DP[1][l],DP[1][k]+C[l])
            if DP[1][l]<=DP[1][min_ind_T2]: min_ind_T2=l
            l+=1
        h=min_ind_T1
        k=min_ind_T2
    return DP[1][n+1]

def min_cost2( O, C, T, L ):
    # tu prosze wpisac wlasna implementacje
    n=len(O)
    way=[[O[i],C[i]] for i in range(n)]
    way.append([0,0])
    way.sort()
    way.append([L,0])
    n+=2
    costs=[[float('inf'),float('inf')] for _ in range(n)]
    costs[0]=[0,0]
    for i in range(1,n):
        j=i-1
        while j>=0 and way[i][0]-way[j][0]<=T:
            costs[i][0]=min(costs[i][0],costs[j][0])
            costs[i][1]=min(costs[i][1],costs[j][1])
            j-=1
        while j>=0 and way[i][0]-way[j][0]<=2*T:
            costs[i][1]=min(costs[i][1],costs[j][0])
            j-=1
        costs[i][0]+=way[i][1]
        costs[i][1]+=way[i][1]
    return costs[n-1][1]





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests = True )
