from zad1testy import runtests

def mergesort(A):
    n=len(A)
    if n==1:
        return A
    a1=A[:n//2]
    a2=A[n//2:]
    a1=mergesort(a1)
    a2=mergesort(a2)
    return merge(a1,a2)


def merge(a1,a2):
    i=j=0
    x=0
    n=len(a1)+len(a2)
    A=[0 for _ in range(n)]
    while i < len(a1) and j < len(a2):
        if a1[i][0]<=a2[j][0]:
            A[x]=a1[i]
            i+=1
        else:
            A[x]=a2[j]
            j+=1
        x+=1
    while i<len(a1):
        A[x]=a1[i]
        x+=1
        i+=1
    while j<len(a2):
        A[x]=a2[j]
        x+=1
        j+=1
    return A

def chaos_index( T ):
    # tu prosze wpisac wlasna implementacje
    for i in range(len(T)):
        T[i]=(T[i],i)
    T=mergesort(T)
    res=0
    for i in range(len(T)):
        res=max(res,abs(i-T[i][1]))
    return res


runtests( chaos_index )
