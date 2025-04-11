from zad12ktesty import runtests 

# funkcja suma tworzy tablice z zapisanymi sumami odleglosci poszczegolnych odcinkow autostrady, a funkkcja F korzysta z obliczonych sum i uzupełnia tablicę dp, gdzie
# dp[i][k] to najkrotszy czas potrzebny na remont autostrady na odcinku od 0 do i, jeśli jest k firm. 

def suma(T):
    n=len(T)
    S=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        S[i][i]=T[i]
        for j in range(i+1,n):
            S[i][j]=S[i][j-1]+T[j]
    return S
    
def F(dp,s,i,k):
    if k==1:
        return s[0][i]
    if dp[i][k]==0:
        mini=float('inf')
        for j in range(i):
            mini=min(max(s[j+1][i],F(dp,s,j,k-1)),mini)
        dp[i][k]=mini
    return dp[i][k]
    

def autostrada( T, k ):
    n=len(T)
    dp=[[0 for _ in range(k+1)] for _ in range(n)] 
    s=suma(T)
    
    return F(dp,s,n-1,k)

runtests ( autostrada,all_tests=True )