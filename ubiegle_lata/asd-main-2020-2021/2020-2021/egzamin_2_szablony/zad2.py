from zad2testy import runtests

# cos zmieilam i nagle zaczelo dzialac


class Node:
  def __init__( self ):   # stwórz węzeł drzewa
    self.edges   = []     # lista węzłów do których są krawędzie
    self.weights = []     # lista wag krawędzi
    self.ids     = []  # lista identyfikatorów krawędzi
    self.sum=0
      
  def addEdge( self, x, w, id ): # dodaj krawędź z tego węzła do węzła x
    self.edges.append( x )       # o wadze w i identyfikatorze id
    self.weights.append( w ) 
    self.ids.append( id )

    
def act_sums(T):
    if T.edges==[]:
        return 0
    for edge in range(len(T.edges)):
        T.sum+=T.weights[edge]
        T.sum+=act_sums(T.edges[edge])
    return T.sum

'''
def albert_einstein(T,best,id,x):  
        for edge in range(len(T.edges)):
            o=T.sum-T.weights[edge]-T.edges[edge].sum
            if abs(o+x-T.edges[edge].sum)<best:
                id=T.ids[edge]
                best=abs(o-T.edges[edge].sum)
            if albert_einstein(T.edges[edge],best,id,x+T.weights[edge]+o)[0]<best:
                best,id=albert_einstein(T.edges[edge],best,id,x+T.weights[edge]+o)
        return best,id
'''

def balance( T ):
    """tu prosze wpisac wlasna implementacje"""
    act_sums(T)
    best=float('inf')
    id=0
    x=T.sum
    def albert_einstein(T): 
        nonlocal best, id
        for edge in range(len(T.edges)):
            o=x-T.weights[edge]-T.edges[edge].sum
            if abs(o-T.edges[edge].sum)<best:
                id=T.ids[edge]
                best=abs(o-T.edges[edge].sum)
            albert_einstein(T.edges[edge])
    albert_einstein(T)
    return id

    
runtests( balance )


