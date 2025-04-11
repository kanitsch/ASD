from egz1Atesty import runtests
from queue import PriorityQueue

def Dijkstra(G,s,wsp=1,const=0):
  n=len(G)
  pq=PriorityQueue()
  d=[float("inf") for _ in range(n)]
  d[s]=0
  pq.put((d[s],s))
  while not pq.empty():
        pri, u=pq.get()
        for v in G[u]:
            if d[v[0]]>d[u]+v[1]*wsp+const:
              d[v[0]]=d[u]+v[1]*wsp+const
              pq.put((d[v[0]],v[0]))
  return d
  
  

def gold(G,V,s,t,r):
  # tu prosze wpisac wlasna implementacje
  n=len(G)
  s_to_i=Dijkstra(G,s)
  t_to_i_modified=Dijkstra(G,t,2,r)
  mini=s_to_i[t]
  for i in range(n):
    mini=min(mini,s_to_i[i]+t_to_i_modified[i]-V[i])
  return mini
  
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
