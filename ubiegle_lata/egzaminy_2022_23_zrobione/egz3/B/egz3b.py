from egz3btesty import runtests

# zlozonosc akceptowalna, zoptymalizowany bruteforce.
# wzorcowka to chyba jakies dzikie dzrzewo przedzialowe
# a jednak nie, ale n^2 działa w podobnym czasie, nawet minimalnie szybciej

def cool(p1,p2):
  if p1[1]<p2[0] or p1[1]>=p2[1] or p1[0]==p2[0]:
    return True
  return False
def uncool( P ):
  # tu prosze wpisac wlasna implementacje
  for i in range(len(P)):
    P[i]=(P[i][0],P[i][1],i)
  P.sort()
  for i in range(len(P)-1):
    a,b,c=P[i]
    p1=(a,b)
    for j in range(i+1,len(P)):
      a,b,d=P[j]
      p2=(a,b)
      if a>p1[1]:
        break
      if not cool(p1,p2):
        return (c,d)

def binary_search2(tab, value):
    _start = 0
    _end = len( tab ) - 1
    while _start <= _end:
        middle = ( _start + _end ) // 2
        if value > tab[ middle ][0]: _start = middle + 1
        else: _end = middle - 1
    if _start==len(tab) or _start<len(tab) and tab[_start][0]>=value:
        return _start-1

def uncool2(P):
  for i in range(len(P)):
    P[i]=(P[i][0],P[i][1],i)
  P.sort()
  for i in range(len(P)):
      j=binary_search2(P,P[i][1])
      if not cool(P[i],P[j]):
        return (P[i][2],P[j][2])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool2, all_tests = True)
