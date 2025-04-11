'''
Karolina Nitsch 421767
Najpierw tworzę listę, w ktorej dla kazdego zadania są wypisane zadania ktore trzeba wykonac przed nim, oraz na koncu ilosc tych zadan.
Tworzę tablicę time wypelniona zerami, ktore oznaczaja ze czas nie jest jeszcze policzony. Jezeli przed jakims zadaniem nie trzeba wykonywac innych to ustamiam time na 1.
Nastepnie dla kazdego zadania uruchamiam funkce uzup, ktora oblicza najkrotszy czas po jakim mozna wykonac dane zadanie. Funkcja ta dziala rekurencyjnie, ale ze spamietywaniem
wynikow, dzieki czemu jest szybsza. Na końcu algorytm zwraca najwiekszy wynik jaki zostal zapisany w tablicy time, ktory oznacza najkrotszy czas po jakim mozna wykonac wszystkie zadania.
Zlozonosc szacuje na O(n^2)'''

from kolutesty import runtests

def lista_zadan(n,L):  # zwraca tablice w ktorej dla kazdego projektu jest tablica projektow ktore trzeba wykonac wczesniej
  t=[[]for _ in range(n)]
  for zad in L:
    x,y=zad
    t[x].append(y)
  for i in t:
    i.append(len(i))
  return t

def uzup(T,n,time,j) :
  if time[j]!=0:
    return time[j]
  lista=T[j]
  maxi=0
  for i in range(len(T[j])-1):
      maxi=max(maxi,uzup(T,n,time,T[j][i]))
  time[j]=maxi+1
  return time[j]
  

def projects(n, L):

  T=lista_zadan(n,L)
  time=[0 for _ in range(n)]
  for j in range(n):
   if T[j][len(T[j])-1]==0:
     time[j]=1
  for j in range(n):
    time[j]=uzup(T,n,time,j)
  

  return max(time)

from collections import deque, defaultdict

def zadania(n,L):
    G=[[] for _ in range(n)]
    prep=[0 for _ in range(n)]
    time=[0 for _ in range(n)]
    for p,q in L:
        G[q].append(p)
        prep[p]+=1
    q=deque()
    for i in  range(n):
        if prep[i]==0:
            q.append(i)
            time[i]=1
    while q:
        u=q.popleft()
        for v in G[u]:
            prep[v]-=1
            if prep[v]==0:
                q.append(v)
                if time[v]<time[u]+1:
                    time[v]=time[u]+1
    return max(time)




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( zadania, all_tests = True)

