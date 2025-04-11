from zad3testy import runtests

def strong_string_n2(T):
    n=len(T)
    maxx=1
    for i in range(n):
        strength=1
        for j in range(i+1,n):
            if T[i]==T[j] or T[i]==T[j][::-1]:
                strength+=1
            maxx=max(maxx,strength)
    return maxx

def heapify(A,n,i):
    l=2*i+1
    r=2*i+2
    max_ind=i
    if l<n and A[l]>A[max_ind]:
        max_ind=l
    if r<n and A[r]>A[max_ind]:
        max_ind=r
    if max_ind!=i:
        A[i],A[max_ind]=A[max_ind],A[i]
        heapify(A,n,max_ind)

def buildheap(A):
    n=len(A)
    for i in range(n//2,-1,-1):
        heapify(A,n,i)

def heapsort(A):
    n=len(A)
    buildheap(A)
    for i in range(n-1,0,-1):
        A[i],A[0]=A[0],A[i]
        heapify(A,i,0)
        
def binsearch(arr,l,r,x):
    if l==r:
        return False
    mid=(l+r)//2
    if arr[mid]==x:
        return True
    if arr[mid]<x:
        return binsearch(arr,mid+1,r,x)
    return binsearch(arr,l,mid,x)
        
def strong_string(T): #nlogn
    n=len(T)
    heapsort(T) #nlogn
    for i in range(n): #n
        s=T[i]
        if binsearch(T,0,n,s[::-1]): #logn
            T[i]=s[::-1]
    heapsort(T) #nlogn
    maxx=1
    s=T[0]
    strength=1
    for i in range(1,n): #n
        if T[i]==T[i-1]:
            strength+=1
        else:
            maxx=max(maxx,strength)
            strength=1
    maxx=max(maxx,strength)
    return maxx
    



# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
