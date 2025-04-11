from zad1testy import runtests
from queue import Queue

class Node:
  def __init__( self ):
    self.left    = None  # lewe podrzewo
    self.right   = None  # prawe poddrzewo
    self.parent  = None  # rodzic drzewa jesli istnieje
    self.value   = None  # przechowywana wartosc
    
def ConvertTree(p):
    # tu prosze wpisac wlasna implementacje
    T=[]
    def tablicuj(p):
        if p!=None:
            tablicuj(p.left)
            T.append(p.value)
            tablicuj(p.right)
    tablicuj(p)
    Q=Queue()
    root=Node()
    root.value=T[0]
    Q.put((T[1],root))
    Q.put((T[2],root))
    i=3
    while not Q.empty():
        ptr=Node()
        ptr.value,ptr.parent=Q.get()
        if ptr.parent.left==None:
            ptr.parent.left=ptr
        else:
            ptr.parent.right=ptr
        if i<len(T):
            Q.put((T[i],ptr))
            i+=1
        if i<len(T):
            Q.put((T[i],ptr))
            i+=1
    
    return root


runtests( ConvertTree )