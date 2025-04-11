from zad1testy import Node, runtests

'''
Karolina Nitsch

program sortuje liste wykorzystujac mergesort, jesli k jest wieksze niż połowa długości listy.
Dla logn<k<n//2 sortuje pierwsze 2k elementow (mergesort) a nastepnie kazde kolejne k elementow i laczy je z ostatnimi 
k elementami posortowanej listy w posortowana liste.
Dla mniejszych wartości k stosuje bubblesort (tylko k iteracji a nie n, bo pozniej lista jest już posortowana. 
Gdyby lista była posortowana zanim wykonają się wszystkie iteracje, to funkcja konczy się wcześniej 
i zwraca posortowaną listę - po to jest flaga) 

zlozonosc:
n*logn dla k>n//2
k*n dla k<=n//2

k = Θ(1):
zlozonosc rzędu n (lub nlogn dla k>n//2)
 
k = Θ(log n) :
zlozonosc rzedu nlogn

k=0(n):
zlozonosc rzedu nlogn

'''

def merge_sorted_lists(a, b):
    if a is None:
        return b
    if b is None:
        return a
    res=Node
    g=res
    while a is not None and b is not None:
        if a.val<b.val:
            g.next=a
            a=a.next
        else:
            g.next=b
            b=b.next
        g=g.next
    if a is not None:
        g.next=a
    else: g.next=b
    return res.next



def split_half(p):
    if p is None:
        return None, None
    slow = p
    fast = p.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    p1=slow.next
    slow.next = None
    return p, p1

def ll_len(p):
    cnt=0
    s=p
    while s is not None:
        cnt+=1
        s=s.next
    return cnt

def mergesort(p):
    if p is None or p.next is None:
        return p
    front, back = split_half(p)
    front = mergesort(front)
    back = mergesort(back)
    return merge_sorted_lists(front, back)

def bubblesort(head,k):
    n=ll_len(head)
    for i in range(k):
        start = head
        flag=False
        for j in range(n-i-1):
            if start.val > start.next.val:
                start.val,start.next.val=start.next.val,start.val
                flag=True
            start=start.next
        if not flag:
            return head
    return head

def split_k_first(head,k):
    p1=head
    for _ in range(k):
        p1=p1.next
    p2=p1.next
    p1.next=None
    return head,p1,p2

def k_sort(head, k):
    ptr1,_,ptr2=split_k_first(head,2*k)
    sortd=mergesort(ptr1)
    cnt=k
    while k<ll_len(ptr2):
        ptr1,_,ptr2=split_k_first(ptr2,k)
        ptr1=mergesort(ptr1)
        sortd,end,k_last = split_k_first(sortd,cnt)
        k_last=merge_sorted_lists(k_last,ptr1)
        end.next=k_last
        cnt+=k

    if ll_len(ptr2)!=0:
        ptr2=mergesort(ptr2)
        sortd=merge_sorted_lists(sortd,ptr2)
    return sortd

def bubblesort2(head,k):
    n=ll_len(head)
    prev = Node
    prev.next = head
    head=prev
    for i in range(k):
        prev=head
        flag=False
        for j in range(n-i-1):
            curr=prev.next
            if curr.val > curr.next.val:
                flag=True
                tmp=curr.next
                curr.next=curr.next.next
                tmp.next=curr
                prev.next=tmp
            prev=prev.next
        if not flag:
            return head.next
    return head.next

def select_sort_ll(p,k): #najwolniej dziala, napisany dla zabawy, zlozonosc taka jak bubblesort
    head=Node
    head.next=p
    p=head
    while p!=None and p.next!=None:
        q=p
        mini=q
        cnt=0
        while q.next!=None and cnt<=k:
            if q.next.val<mini.next.val:
                mini=q
            q=q.next
            cnt+=1
        tmp=mini.next
        mini.next=mini.next.next
        tmp.next=p.next
        p.next=tmp
        p=p.next
    return head.next


def SortH(p,k):
    n=ll_len(p)
    if 2**k<=n:
        p=bubblesort2(p,k)
    elif k < n//2:
        p=k_sort(p,k)
    else:
        p=mergesort(p)
    return p


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
