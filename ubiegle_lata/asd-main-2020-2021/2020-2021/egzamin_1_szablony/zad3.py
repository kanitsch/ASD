from zad3testy import runtests
from queue import PriorityQueue
from copy import deepcopy

# glupi monos
def kintersect( A, k ):
  """Miejsce na Twoją implementację"""
  B=deepcopy(A)
  A.sort()
  n=len(A)
  cnt=0
  pq=PriorityQueue()
  res=0
  pocz=0
  kon=0
  for i in range(n):
    cnt+=1
    start=A[i][0]
    pq.put(A[i][1])
    if cnt==k:
      end=pq.get()
      if end-start>res:
        res=end-start
        pocz=start
        kon=end
      cnt-=1
  lista=[]
  for i in range(n):
    if B[i][0]<=pocz and B[i][1]>=kon:
      lista.append(i)

  return lista

runtests( kintersect )