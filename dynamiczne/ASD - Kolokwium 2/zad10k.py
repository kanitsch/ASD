from zad10ktesty import runtests
from math import sqrt, floor

def dywany ( N ):
    #Tutaj proszę wpisać własną implementację
    dp=[float('inf') for _ in range(N+1)]
    arrays=[[] for _ in range(N+1)]
    dp[0]=0
    for i in range(1,N+1):
        k=floor(sqrt(i))
        for j in range(i,N+1):
            x=j//k**2
            l=j-x*k**2
            if x+dp[l]<dp[j]:
                dp[j]=dp[l]+x
                arrays[j]=x*[k]+arrays[l]
            
    return arrays[-1]



runtests( dywany )

