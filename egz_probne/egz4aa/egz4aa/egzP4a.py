
from egzP4atesty import runtests

def binsearch(ciag,liczba):
    p=len(ciag)
    l=0
    while l+1<p:
        mid=(l+p)//2
        if ciag[mid]>=liczba and ciag[mid-1]<liczba:
            return mid
        elif ciag[mid]>=liczba:
            p=mid
        else:
            l=mid+1
    if ciag[l]<liczba<=ciag[p]:
        return p
    return l

def mosty(T):
    T.sort()
    n=len(T)
    ciag=[T[0][1]]
    for i in range(1,n):
        if T[i][1]>=ciag[-1]:
            ciag.append(T[i][1])
        else:
            x=binsearch(ciag,T[i][1]) #binsearch zwraca indeks najmniejszej liczby w ciagu wiekszej lub rownej T[i][1]
            ciag[x]=T[i][1]
    return len(ciag)

def mosty_n2 ( T ):
    #tutaj proszę wpisać własną implementację 
    T.sort()
    n=len(T)
    dp=[0 for _ in range(n)]
    for i in range(n):
        v=T[i][1]
        maxx=0
        for j in range(i+1):
           if dp[j]>maxx and T[j][1]<=T[i][1]:
               maxx=dp[j]
        dp[i]=maxx+1
        
    return max(dp)

runtests ( mosty, all_tests=True )