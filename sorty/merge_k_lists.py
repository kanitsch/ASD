
class Node:
  def __init__(self):
    self.val = None
    self.next = None


def tab2list(t):
    n = len(t)
    p = None

    for i in range(n-1,-1,-1):
        q = Node()
        q.val = t[i]
        q.next = p
        p = q

    return p


def list2tab(l):
    t = []
    while l!=None:
        t.append(l.val)
        l = l.next

    return t




def parent(i):
    return (i-1)//2
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2

def heapify(T,n,i):
    l=left(i)
    r=right(i)
    min_ind=i
    if l<n and T[l].val<T[min_ind].val:
        min_ind=l
    if r<n and T[r].val<T[min_ind].val:
        min_ind=r
    if min_ind!=i:
        T[min_ind],T[i]=T[i],T[min_ind]
        heapify(T,n,min_ind)
        
def buildheap(T,n):
    for i in range(parent(n-1),-1,-1):
        heapify(T,n,i)
            
def merge_lists(T):
    n=len(T)
    buildheap(T,n)
    g=Node()
    start=g
    while n:
        g.next=T[0]
        T[0]=T[0].next
        if T[0]==None:
            T[0],T[n-1]=T[n-1],T[0]
            n-=1
        heapify(T,n,0)
        g=g.next
    return start.next

p1=tab2list([2,4,7,48,90])
p2=tab2list([5,7,24,58])
p3=tab2list([78,79,456,600,798,900])
p4=tab2list([1,2,3,4,5,6,7,8,9,10])
T=[p1,p2,p3,p4]
res=merge_lists(T)
res=list2tab(res)
print(res)
            
        
    
    