from egz1btesty import runtests



def kstrong_brut( T, k):
  # tu prosze wpisac wlasna implementacje
  n=len(T)
  maxsum=0
  for i in range(n-1):
    for j in range(i+1,n+1):
      suma=0
      t=T[i:j]
      t.sort()
      x=0
      while x<k and x<len(t) and t[x]<0:
        x+=1
      while x<len(t):
            suma+=t[x]
            x+=1
      maxsum=max(suma,maxsum)
   
      
      
  
  return maxsum

def kstrong(T,k):
  n=len(T)
  maxsum=0
  dp=[[0 for _ in range(k+1)] for _ in range(n)]
  dp[0][0]=max(T[0],0)
  for i in range(1,n):
    dp[i][0]=max(dp[i-1][0]+T[i],0)
    maxsum=max(maxsum,dp[i][0])
    for j in range(1,k+1):
      dp[i][j]=max(0,dp[i-1][j]+T[i],dp[i-1][j-1])
      maxsum=max(maxsum,dp[i][j])
  return maxsum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
