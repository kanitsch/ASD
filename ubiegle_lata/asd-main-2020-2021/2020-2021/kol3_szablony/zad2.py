from zad2testy import runtests

class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

def cutthetree(T):
    """tu prosze wpisac wlasna implementacje"""
    def rek(T):
        if T.left==None and T.right==None:
            return float('inf')
        if T.right!=None and T.left!=None:
            return min(T.value,rek(T.left)+rek(T.right))
        if T.left!=None:
            return min(T.value,rek(T.left))
        if T.right!=None:
            return T.value
    return rek(T.left)+rek(T.right)


    
runtests(cutthetree)


