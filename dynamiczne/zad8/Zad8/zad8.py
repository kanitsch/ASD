''' Karolina Nitsch
Tworzę tablicę f o wymiarach n x m, w której zapisuję wyniki obliczanej funkcji.
f[i][j] oznacza najmniejszą sumę odległości biurowców z pozycji X[0]...X[i], do parkingów z pozycji Y[0]...Y[j] spełniającą warunki zadania.
Przy obliczaniu wartości tablicy uwzględniam, że biurowiec z pozycji X[i] może mieć parking z pozycji Y[j] lub wcześniejszy, ale nie może być wcześniej niż na pozycji Y[i] 
(wtedy dla biurowców z poprzednich pozycji byłoby za mało parkingów). Wiadomo, że f[0][0] to odległość zerowego biurowca
do zerowej działki, f[0][1] - odległość zerowego biurowca do zerowej lub pierwszej działki (szukam minimum), itd. W ten sposób wypełniam pierwszy wiersz.
Jako f[i][j] zapisuję minimum z f[i-1][j-1] (czyli najmniejsza suma odległości biurowców z wcześniejszych pozycji do parkingów kończących się na pozycji Y[j-1] lub wcześniej) + odległość i-tego biurowca do j-tej działki 
oraz z f[i][j-1] (najmniejsza suma odległości, jeżeli i-ty biurowiec ma parking wcześniejszy niż j-ty). Dzięki temu zapisywana suma odległości parkingów od biurowców jest minimalna i na końcu wystarczy odczytać i zwrócić f[n-1][m-1].
Algorytm ma złożoność obliczeniową i pamięciową O(n*m)
'''


from zad8testy import runtests

def parking(X,Y):
  n=len(X)
  m=len(Y)
  f=[[float('inf') for _ in range(m)] for _ in range(n)]
  f[0][0]=abs(X[0]-Y[0])
  for j in range(1,m-n+1):
    f[0][j]=min(f[0][j-1],abs(X[0]-Y[j]))
  for i in range(1,n):
    for j in range(i,m-n+i+1):
      f[i][j]=min(f[i-1][j-1]+abs(X[i]-Y[j]),f[i][j-1])
      
  return f[n-1][m-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
