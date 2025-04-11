
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

def mergesort(p):
    if p is None or p.next is None:
        return p
    front, back = split_half(p)
    front = mergesort(front)
    back = mergesort(back)
    return merge_sorted_lists(front, back)

l=[3,5,8,67,54,23,9,1,987,4]
l=tab2list(l)
l=mergesort(l)
l=list2tab(l)
print(l)