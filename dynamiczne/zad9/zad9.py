'''
Karolina Nitsch
Algorytm polega na uzupełnianiu tablicy max_trip o wymiarach n x m najdłuższymi wycieczkami z danego szczytu (max_trip[i][j] to najdłuższa wycieczka ze szczytu M[i][j])
Jednocześnie obliczana jest najdłuższa możliwa trasa. Iterując po tablicy max_trip, jeżeli napotykamy nieodwiedzony wcześniej szczyt (wartość max_trip[i][j] jest równa 0)
to wywołujemy funkcję visit, która zwraca najdłuższą trasę z tego szczytu i uzupełnia tablicę obliczonymi podczas wywoływania rekurencyjnego wartościami dla innych szczytów. 
Dzięki temu unikamy obliczania wielokrotnie długości tych samych tras.
Złożoność obliczeniowa wynosi O(n*m), pamięciowa również O(n*m)
'''



from zad9testy import runtests

def trip(M):
  def visit(M,max_trip,i,j,n,m):
    if max_trip[i][j]!=0:
      return max_trip[i][j]
    maxi=1
    for y,x in [(0,1),(0,-1),(1,0),(-1,0)]:
      if 0<=i+y<n and 0<=j+x<m and M[i+y][j+x]>M[i][j]:
        maxi=max(maxi,1+visit(M,max_trip,i+y,j+x,n,m))
    max_trip[i][j]=maxi
    return maxi
          
        
  n=len(M)
  m=len(M[0])
  max_trip = [[0 for _ in range(m)] for _ in range(n)]
  maxlen=1
  for i in range(n):
    for j in range(m):
      if max_trip[i][j]==0:
        maxlen=max(maxlen,visit(M,max_trip,i,j,n,m))
  return maxlen
          
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
