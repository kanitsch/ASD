# Karolina Nitsch
# Funkcja opiera się na Algorytmie Dijkstry, ale najkrótsze odległości są zapisywane w tablicy dwuwymiarowej. 
# Każdy wierzchołek ma w niej zapisaną najkrótszą odległość w przypadku, gdy ostatni krok był zwyczajny i w przypadku gdy był dwumilowy.
# Dla każdego wierzchołka -"u" wyciąganego z kolejki priorytetowej, aktualizowane są najkrótsze trasy do ich sąsiadów -"v" zwyczajnym krokiem 
# (wtedy poprzedni krok mógł być zwyczajny lub dwumilowy)
# a także do sąsiadów jego sąsiadów - "x" przy użyciu dwumilowych butów. Dwumilowe buty nie mogą zostać użyte dwa razy pod rząd, ponieważ przy relaksacji 
# w przypadku skoków dwumilowych biorę pod uwagę tylko sumę trasy dojścia do wierzchołka u, w której ostatni odcinek został pokonany 
# w sposób zwyczajny oraz dwumilowego skoku z u do x.
# Funkcja zwraca minimum z zapisanych odległości z wierzchołka "s" do "w" (z ostatnim krokiem zwykłym lub dwumilowym)
# Złożoność szacuję na O(V^3), gdzie V to liczba wierzchołków.

from zad6testy import runtests
from queue import PriorityQueue

def jumper( G, s, w ):
    n=len(G)
    d=[[float('inf'),float('inf')] for _ in range(n)] #pierwszy element to najkrotsza odleglosć od s jezeli ostatni krok był zwyczajny, a drugi jeżeli był dwumilowy
    pq=PriorityQueue()
    pq.put((0,s))
    d[s][0]=0
    while not pq.empty():
        (dist_u,u) = pq.get()
        if u==w:
           return min(d[w])    
        for v in range(n):
            if G[u][v]>0:
                if d[v][0]>min(d[u])+G[u][v]:
                    d[v][0]=min(d[u])+G[u][v]
                    pq.put((d[v][0],v))          
                for x in range(n):
                    if G[v][x]>0:
                        dwumil=max(G[u][v],G[v][x])
                        if d[x][1]>d[u][0]+dwumil:
                            d[x][1]=d[u][0]+dwumil
                            pq.put((d[x][1],x))
    return min(d[w])



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )