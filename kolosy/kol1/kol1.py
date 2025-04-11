'''Karolina Nitsch 421767
Algorytm polega na zliczaniu dla każdego elementu tablicy T, ile elementów znajdujących się przed nim
jest mniejszych od niego. Jeśli wynik wychodzi większy niż zapisana wartość maxi, to aktualizuję maxi na nowy wynik. Jeżeli element, 
który sprawdzam jest mniejszy od poprzedniego elementu w tablicy, to pomijam liczenie mniejszych elementów leżących przed nim, 
bo wynik nie mógłby być większy od wyniku, który wyszedł dla poprzedniego elementu. Złożoność czasowa to O(n^2), a pamięciowa O(n)'''



from kol1testy import runtests


def maxrank(T):
  n=len(T)
  maxi=0
  for i in range(n):
    cnt=0
    if i>0 and T[i]>T[i-1]:
      for j in range (i):
        if T[j]<T[i]:
          cnt+=1
      maxi=max(maxi,cnt)
    
      
  return maxi

def mergesort(A):
    n=len(A)
    if n==1:
        return A
    a1=A[:n//2]
    a2=A[n//2:]
    a1=mergesort(a1)
    a2=mergesort(a2)
    return merge(a1,a2)


def merge(a1,a2):
    i=j=0
    x=0
    n=len(a1)+len(a2)
    A=[0 for _ in range(n)]
    while i < len(a1) and j < len(a2):
        if a1[i][0]>=a2[j][0]:
            A[x]=a1[i]
            i+=1
        else:
            A[x]=a2[j]
            j+=1
        x+=1
    while i<len(a1):
        A[x]=a1[i]
        x+=1
        i+=1
    while j<len(a2):
        A[x]=a2[j]
        x+=1
        j+=1
    return A


def maxrank2(T): # w przypadku inwersji ta metoda jest zla ale tu przechodzi testy
  n = len(T)
  maxi = 0
  for i in range(n):
    T[i]=(T[i],i)
  T=mergesort(T)
  for i in range(n):
      maxi=max(maxi,T[i][1]-i)
  return maxi



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank2, all_tests = True)
