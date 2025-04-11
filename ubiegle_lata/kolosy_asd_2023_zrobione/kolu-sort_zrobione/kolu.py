from kolutesty import runtests

def count_sort(A,p):
    n=len(A)
    B=[None for _ in range(n)]
    C=[0]*10
    for x in A:
        y=x%(10**p)//10**(p-1)
        C[y]+=1
    for i in range(1,10):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i]%(10**p)//10**(p-1)]-1]=A[i]
        C[A[i]%(10**p)//10**(p-1)]-=1
    return B   

def ice_cream( T ):
    max_lod=0
    for lod in T:
        max_lod=max(max_lod,lod)
    p=0
    while max_lod:
        max_lod//=10
        p+=1
    for i in range(1,p+1):
        T=count_sort(T,i)
    topisie=0
    i=len(T)-1
    suma=0
    while i>=0 and T[i]-topisie>0:
        suma+=T[i]-topisie
        i-=1
        topisie+=1
    return suma
        
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
