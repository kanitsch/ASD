def parent(c):
    return (c-1)//2

def heapInsert(heap,n):
    heap.append(n)
    pos=len(heap)-1
    par=parent(pos)
    while pos>0 and heap[par]<heap[pos]:
        heap[par], heap[pos] = heap[pos], heap[par]
        pos=par
        par=parent(pos)
    return heap

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

T=[1,-1,3,5,200,100,400,53,67,21,6,75,30]
buildheap(T)
print(T)
T.insert(0,50)
heapify(T,len(T),0)
print(T)
T[0],T[-1]=T[-1],T[0]
T.pop()
heapify(T,len(T),0)
print(T)

