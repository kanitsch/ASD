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


A=[3,5,7,3,8,67,8,90,34,2]
heapify(A,len(A),0)
print(A)
heapsort(A)
print(A)

T = [16,5,4,9,3,-10,20]
buildheap(T)
print(T)