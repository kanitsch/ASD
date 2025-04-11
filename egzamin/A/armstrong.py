def armstrong1( B, G, s, t):
  # tu prosze wpisac wlasna implementacje
  n=len(G)
  d=[[float('inf'),float('inf')] for _ in range(n)]
  d[s][0]=0
  B=rowery(B,n)
  G=lista_sasiedztwa(G)
  pq=PriorityQueue()
  pq.put((0,s,0))
  if B[s]:
    pq.put((0,s,B[s]))
    d[s][1]=0
    
  while not pq.empty():
    odl,u,rower=pq.get()
    for sasiad in G[u]:
      v,x=sasiad
      if rower:  
        if d[v][1]>odl+x*rower:
          d[v][1]=odl+x*rower
          pq.put((odl+x*rower,v,rower))
      else:
        if d[v][0]>odl+x:
          d[v][0]=odl+x
          pq.put((d[v][0],v,0))
        if B[u]:
          new_bckl=B[u]
          if d[v][1]>odl+new_bckl*x:
            d[v][1]=odl+new_bckl*x
            pq.put((odl+new_bckl*x,v,new_bckl))

  return int(min(d[t]))