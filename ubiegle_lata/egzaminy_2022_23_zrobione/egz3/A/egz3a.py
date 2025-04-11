from egz3atesty import runtests
from queue import PriorityQueue

'''
Algorytm dijkstry ale dla każdego wierzchołka jest 0-16 poziomów zmęczenia. jeżeli po przejściu kolejnej krawędzi poziom zmęczenia przekroczyłby 16, to konieczny jest odpoczynek 8 godz
który doliczany jest do odległości, a poziom zmęczenia się resetuje. zlozonosc wynosi n^2 (zamiana na liste sasiedztwa) + nlogn (algorytm dijkstry, bo liczba krawedzi lest rzedu O(n))
'''

def lis_sas(G):
  n=len(G)
  L=[[] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if G[i][j]!=-1:
        L[i].append((j,G[i][j]))
  return L

def goodknight( G, s, t ):
  # tu prosze wpisac wlasna implementacje
  n=len(G)
  L=lis_sas(G)
  dp=[[float('inf') for _ in range(17)] for _ in range(n)]
  dp[s][0]=0
  pq=PriorityQueue()
  pq.put((0,s,0))
  while not pq.empty():
    x,u,z=pq.get()
    for v,d in L[u]:
        if z+d<=16:
          if dp[v][z+d]>dp[u][z]+d:
            dp[v][z+d]=dp[u][z]+d
            pq.put((dp[v][z+d],v,z+d))
        else:
          if dp[v][d]>dp[u][z]+d+8:
            dp[v][d]=dp[u][z]+d+8
            pq.put((dp[v][d],v,d))
  return min(dp[t])


def floyd_warshall_marshall(S):
    n=len(S)
    for k in range(n):
        for x in range(n):
            for y in range(n):
                S[x][y]=min(S[x][y], S[x][k]+S[k][y])
    return S

def prep(M):
  n=len(M)
  for i in range(n):
    for j in range(n):
      if i!=j and M[i][j]==-1:
        M[i][j]=float('inf')
      elif i==j:
        M[i][i]=0
  return M

def akcept(G,s,t):
  prep(G)
  G=floyd_warshall_marshall(G)
  n=len(G)
  for i in range(n):
    for j in range(n):
      if i!=j and G[i][j]>16:
        G[i][j]=float('inf')
      elif i!=j:
        G[i][j]+=8
  G=floyd_warshall_marshall(G)
  return G[s][t]-8


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
