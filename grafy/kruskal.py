class Node:
    def __init__(self,value):
        self.val=value
        self.parent=self
        self.rank=0
        
def find(x):
    if x.parent!=x:
        x.parent=find(x.parent)
    return x.parent

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y: return
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1
            
def kruskal(G,n):
    G.sort(key=lambda x: x[2])
    V=[Node(i) for i in range(n)]
    A=[]
    for e in G:
        u,v,c=e
        if find(V[u])!=find(V[v]):
            union(V[u],V[v])
            A.append(e)
    return A





E=[(1,0,1),(0,2,3),(2,5,6),(3,5,2),(2,3,4),(3,4,7),(1,3,5),(1,4,8)]
print(kruskal(E,6))