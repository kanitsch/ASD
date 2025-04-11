from egz2atesty import runtests

# to zadanie było pozniej jako offline 3 2023/24 (sorty)

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
  return n-mini+1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
