'''szukamy mediany za pomoca dwoch kopcow'''

def heapify_min(A,n,i):
    l=2*i+1
    r=2*i+2
    min_ind=i
    if l<n and A[l]<A[min_ind]:
        min_ind=l
    if r<n and A[r]<A[min_ind]:
        min_ind=r
    if min_ind!=i:
        A[i],A[min_ind]=A[min_ind],A[i]
        heapify_min(A, n, min_ind)

def heapify_max(A,n,i):
    l=2*i+1
    r=2*i+2
    max_ind=i
    if l<n and A[l]>A[max_ind]:
        max_ind=l
    if r<n and A[r]>A[max_ind]:
        max_ind=r
    if max_ind!=i:
        A[i],A[max_ind]=A[max_ind],A[i]
        heapify_max(A, n, max_ind)

def buildheap_max(A):
    n=len(A)
    for i in range(n//2,-1,-1):
        heapify_max(A, n, i)


def buildheap_min(A):
    n=len(A)
    for i in range(n//2,-1,-1):
        heapify_min(A, n, i)

def heapsort(A):
    n=len(A)
    buildheap_max(A)
    for i in range(n-1,0,-1):
        A[i],A[0]=A[0],A[i]
        heapify_max(A,i,0)

T=[3,56,32,48,9,65,3,2,78,4,34,94,8]
heapsort(T)
n=len(T)//2
x=None
if len(T)%2!=0:
    x=T[n]
    maxheap,minheap=T[:n],T[n+1:] #mialo byc na odwrot
else:
    maxheap,minheap=T[:n],T[n:]
buildheap_max(maxheap)
print(minheap,maxheap,x)

def removemedian(minheap,maxheap):
    global x
    if x!=None:
        median=x
        x=None
        return median
    if len(minheap)==0:
        return None
    median=(minheap[0]+maxheap[0])//2
    if len(minheap)>1:
        minheap[0],minheap[-1]=minheap[-1],minheap[0]
        minheap.pop()
        heapify_min(minheap,len(minheap),0)
        maxheap[0],maxheap[-1]=maxheap[-1],maxheap[0]
        maxheap.pop()
        heapify_max(maxheap,len(maxheap),0)
    else:
        minheap=[]
        maxheap=[]
    return median

def parent(i):
    return (i-1)//2

def maxheapInsert(heap,n):
    heap.append(n)
    pos=len(heap)-1
    par=parent(pos)
    while pos>0 and heap[par]<heap[pos]:
        heap[par], heap[pos] = heap[pos], heap[par]
        pos=par
        par=parent(pos)
    return heap

def minheapInsert(heap,n):
    heap.append(n)
    pos=len(heap)-1
    par=parent(pos)
    while pos>0 and heap[par]>heap[pos]:
        heap[par], heap[pos] = heap[pos], heap[par]
        pos=par
        par=parent(pos)
    return heap
def insert(minheap,maxheap,to_insert):
    global x
    if x!=None:
        if to_insert>=x:
            minheapInsert(minheap,to_insert)
            maxheapInsert(maxheap,x)
        else:
            maxheapInsert(maxheap,to_insert)
            minheapInsert(minheap,x)
        x=None
    else:
        if maxheap[0]<=to_insert<=minheap[0]:
            x=to_insert
        elif maxheap[0]>to_insert:
            x=maxheap[0]
            maxheap[0]=to_insert
            heapify_max(maxheap,len(maxheap),0)
        else:
            x = minheap[0]
            minheap[0] = to_insert
            heapify_min(minheap, len(minheap), 0)



print(removemedian(minheap,maxheap))
print(minheap,maxheap,x)
print(removemedian(minheap,maxheap))
print(minheap,maxheap,x)
insert(minheap,maxheap,10)
print(minheap,maxheap,x)
insert(minheap,maxheap,20)
print(minheap,maxheap,x)
