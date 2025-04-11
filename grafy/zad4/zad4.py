'''
Karolina Nitsch
Funkcja Flight najpierw modyfikuje liste L, tak aby zawierala krawedzie w obie strony, czyli łączy podaną listę z nową listą, w której wierzchołki są podane w odwrotnej kolejności.
Następnie sortuje ją, aby łatwiej było wyszukiwać wierzchołki. Główna część to funkcja rekurencyjna, w której x to punkt w którym się znajdujemy a y to cel.
(Jeżeli x=y to osiągnęliśmy cel i funkcja rek zwraca True). Dodatkowo jako parametr funkcji rek przekazuję przedział w którym musi się mieścić pułap, oraz tablicę
visited, w której zapisywane są odwiedzone wierzchołki (aby do nich nie wracać, bo wtedy powstawałyby cykle i funkcja mogłaby się wywoływać w nieskończoność - aż do przepełnienina stosu)
funkcja rek wyszukuje binarnie pierwszą w tablicy L krawędż wychodzącą z wierzchołka x i sprawdza po kolei dla każdej takiej krawędzi, czy mieści się w przedziale i czy nie prowadzi do już odwiedzonego wierzchołka.
Jeżeli warunki są spełnione to wywołuje się rekurencyjnie ze zaktualizowaną listą visited, przedziałem i z nowym wierzchołkiem x. W przypadku, gdy nie osiągnęliśmy celu i nie jest możliwy dalszy krok, to wracamy do ostatniego 
punktu, w którym było to możliwe, a jeśli takiego nie ma, to funkcja zwraca False. Złożoność czasową szacuję na O(n!)

flight2 chyba jest lepsze (na pewno krótsze i prostsze)
'''


from zad4testy import runtests

def partition(T,p,r,index):
    x=T[r][index]
    i=p-1
    for j in range(p,r):
        if T[j][index]<x:
            i+=1
            T[j],T[i]=T[i],T[j]
    i+=1
    T[r],T[i]=T[i],T[r]
    return i

def qs_logn(T,p,r):
    while p<r:
        q=partition(T,p,r,0)
        if (q-p)>(r-q):
            qs_logn(T,q+1,r)
            r=q-1
        else:
            qs_logn(T,p,q-1)
            p=q+1
    return T
            
def binsearch(T,l,r,x):
  while l<=r:
    mid=(l+r)//2
    if T[mid][0]==x:
      while mid>0 and T[mid-1][0]==x:
        mid-=1
      return mid
    elif T[mid][0]<x:
      l=mid+1
    else:
      r=mid-1
  return -1

def rev_list(L):
  newtab=[]
  for el in L:
    newtuple=(el[1],el[0],el[2])
    newtab.append(newtuple)
  return newtab

def Flight(L,x,y,t):
  # tu prosze wpisac wlasna implementacje
  L_rev=rev_list(L)
  L+=L_rev
  L=qs_logn(L,0,len(L)-1)
  visited=[x]
  def rek(L,x,y,t,przedzial,visited):
    if x==y:
      return True
    ind=binsearch(L,0,len(L)-1,x)
    if ind!=-1:
      while ind<len(L) and L[ind][0]==x:
        if L[ind][1] not in visited:
          r1=max(L[ind][2]-t,przedzial[0])
          r2=min(L[ind][2]+t, przedzial[1])
          if r1<=r2:
            #visited.append(L[ind][0])
            if rek(L,L[ind][1],y,t,(r1,r2),visited+[L[ind][0]]):
              return True
        ind+=1
    return False

  
  return rek(L,x,y,t,(0,float('inf')),visited) 

def graf(L):
  n=len(L)
  edgelist=[[]for _ in range(n)]
  for el in L:
        edgelist[el[0]].append([el[1],el[2]])
        edgelist[el[1]].append([el[0],el[2]])
  return edgelist

def Flight2(L,x,y,t):
    def DFS_Visit(G,u,low,high,visited):
        if u==y:
          return True
        for v,p in G[u]:
            if v not in visited and min(p+t,high)>=max(p-t,low):
                if DFS_Visit(G,v,max(p-t,low),min(p+t,high),visited+[v]):
                  return True
        return False
    G=graf(L)
    n=len(G)
    visited=[x]
    return DFS_Visit(G,x,0,float('inf'),visited)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight2, all_tests = True )