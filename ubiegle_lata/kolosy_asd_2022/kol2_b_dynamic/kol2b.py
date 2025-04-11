from kol2btesty import runtests

# mam lepsze rozwiazanie w offline9 2023 ale nie pamietam czy pisalam go sama czy przekopiowalam

def min_cost( O, C, T, L ):
    n=len(O)
    for i in range(n):
        O[i]=(O[i],C[i])
    O.append((L,0))
    O.append((0,0))
    n+=2
    O.sort()
    dp=[[float('inf'),float('inf')] for _ in range(n)]
    dp[0][0]=0
    i=0
    while i<n:
        j=1
        min_ind=i+j
        while i+j<n and O[i+j][0]-O[i][0]<=T:
            dp[i+j][0]=min(dp[i+j][0],dp[i][0]+O[i+j][1])
            dp[i+j][1]=min(dp[i+j][1],dp[i+j][0],dp[i][1]+O[i+j][1])
            if dp[i+j][1]<dp[min_ind][1]:
                min_ind=i+j
            j+=1
        while i+j<n and O[i+j][0]-O[i][0]<=2*T:
            dp[i+j][1]=min(dp[i+j][1],dp[i][0]+O[i+j][1])
            j+=1
        i=min_ind
            
        
    return dp[n-1][1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
