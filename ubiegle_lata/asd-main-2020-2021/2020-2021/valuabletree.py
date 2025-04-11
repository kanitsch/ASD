from zad2_testy import runtests

class Node:
    def __init__(self):

        self.left= None  # lewe poddrzewo
        self.leftval = 0
        self.right= None  # prawe poddrzewo
        self.rightval = 0 # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X= None  # miejsce na dodatkowe dane

def valuableTree(A,k):
    def rek(A,k,l):
        if A==None:
            return -float('inf')
        if l==0:
            return 0
        if A.left==None and A.right==None:
            return -float('inf')
        if A.X and A.X[l]!=None:
            return A.X[l]
        if not A.X:
            A.X=[None for _ in range(k+1)]
        A.X[l]=max(rek(A.left,k,l-1)+A.leftval,rek(A.right,k,l-1)+A.rightval)
        for j in range(l-1):
            A.X[l]=max(A.X[l],rek(A.left,k,j)+A.leftval+A.rightval+rek(A.right,k,l-2-j))
        return A.X[l]
    def sol(A,k):
        nonlocal maxx
        maxx=max(maxx,rek(A,k,k))
        if A.left: sol(A.left,k)
        if A.right: sol(A.right,k)
    maxx=-float('inf')
    sol(A,k)
    return maxx

runtests(valuableTree)