from zad2testy import runtests
from queue import  PriorityQueue

go=[(0,1),(1,0),(0,-1),(-1,0)]
velocity=[60,40,30]

def Dijkstra(G,A):
  n=len(G)
  d=[[[[float('inf') for _ in range(4)] for _ in range(3)] for _ in range(len(G[0]))] for _ in range(n)] # y x predkosc kierunek
  pq=PriorityQueue()
  d[A[1]][A[0]][0][0]=0
  pq.put((0,A[1],A[0],0,0))

  while not pq.empty():
        odl,y,x,v,dir=pq.get()
        obr=(dir+1)%4
        if d[y][x][0][obr]>odl+45:
            d[y][x][0][obr]=odl+45
            pq.put((odl+45,y,x,0,obr))
        obr=(dir-1)%4
        if d[y][x][0][obr]>odl+45:
            d[y][x][0][obr]=odl+45
            pq.put((odl+45,y,x,0,obr))
        if G[y+go[dir][0]][x+go[dir][1]]!='X':
            if d[y+go[dir][0]][x+go[dir][1]][min(v+1,2)][dir]>odl+velocity[v]:
                d[y + go[dir][0]][x + go[dir][1]][min(v + 1, 2)][dir] = odl + velocity[v]
                pq.put((odl+velocity[v],y+go[dir][0],x+go[dir][1],min(v+1,2),dir))

  return d
def robot( L, A, B ):
    """tu prosze wpisac wlasna implementacje"""
    d=Dijkstra(L,A)
    res=float('inf')
    for i in range(3):
        res=min(res,min(d[B[1]][B[0]][i]))
    if res==float('inf'):
        return None
    return res

    
runtests( robot )


