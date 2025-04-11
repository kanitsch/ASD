'''Karolina Nitsch 421767
Algorytm jest oparty o metodę sortowania przez zliczanie, ale nie sortuje danych, tylko zlicza ile jest elementów o współrzędnych większych lub równych.
Dla każdego punktu pi zliczam punkty pj takie że xj>=xi lub yj>=yi. Jeżeli jakiś punkt jest najsilniejszy, to nie ma innych punktów które mają jednocześnie obie współrzędne większe niż ten punkt.
Zatem z zasady włączeń i wyłączeń liczba punktów które punkt pi(xi,yi) dominuje to n-x-y+1, gdzie n to liczba wszystkich punktów, x-liczba punktów o współrzędnej x większej lub równej xi, 
y-liczba punktów o współrzędnej y większej lub równej yi. Na koniec trzeba dodać 1 ponieważ punkt pi został odjęty 2 razy. Aby znalezc liczbe zdominowanych punktów przez najsilniejszy z nich obliczam x+y dla każdego punktu i szukam minimum.
Dla punktów, które nie są najsilniejsze, wartość x+y wyjdzie większa niż ilość punktów o większej współrzędnej x lub y, co nie przeszkadza w znalezieniu szukanego punktu.
Algorytm ma złożoność liniową.'''



from zad3testy import runtests

def counting(A,n,co): #funkcja liczy ile jest elementow o wiekszej lub równej współrzędnej (co - numer wspolrzednej, 0 - x, 1 - y)
  C=[0 for _ in range (n+1)] #tworze tablice w ktorej bede zliczac ilosc punktow o wspolrzednej równej indeksowi tej tablicy
  for j in range(n):
    C[A[j][co]]+=1
  for i in range(n-1,-1,-1): #teraz dla kazdego indeksu dodaje ilosc punktow o wiekszej wspolrzednej
    C[i]+=C[i+1]
  return C 

def dominance(P):
  n=len(P)
  cx=counting(P,n,0)
  cy=counting(P,n,1)
  mini=n
  for i in range(n):  #szukam punktu dla którego jest najmniej punktów o większej lub równej współrzędnej x lub y
    cnt=cx[P[i][0]]+cy[P[i][1]]
    mini=min(mini,cnt)
  return n-mini+1 #nie ma punktów które mają jednocześnie większą współrzędną x i y od najsilniejszego z nich, jednak trzeba dodać 1, ponieważ najsilniejszy punkt został policzony 2 razy podczas liczenia mini


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )

