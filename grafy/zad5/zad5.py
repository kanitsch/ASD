'''
Karolina Nitsch
Funkcja przekształca podaną listę krawędzi E na listę sąsiedztwa, w której zapisany jest czas podróży między planetami (również jeśli czas wynosi 0, bo obie planety znajdują się w okolicy osobliwości)
Następnie przy pomocy kolejki priorytetowej wykonuje algorytm Dijkstry, zapisując odwiedzoe planety w tablicy visited
a najmniejsze odległości z a do poszczególnych wierzchołków w tablicy d.
Program wyjmuje z kolejki wierzchołek o najkrótszym czasie dojścia, który nie był jeszcze odwiedzony i dla każdego sąsiadującego wierzchołka wykonuje funkcję wewnętrzną relax,
która aktualizuje czasy dojścia do poszczególnyych wierzchołków i jeśli się one zmieniły, to dokłada je z nowym, krótszym czasem do kolejki. Wierzchołek zostaje zapisany jako odwiedzony.
Jeśli kolejka stanie się pusta przed dotarciem do wierzchołka b, to funkcja zwraca None. Jeżeli uda się dotrzeć do wierzchołka b, to zwracany jest najkrótszy czas dojścia od a do b 
Algorytm ma złożoność O(ElogV), gdzie E to liczba krawędzi(bezpośrednich przelotów) a V liczba wierzchołków(planet)

to rozwiazanie bylo jakies dziwne, dlaczego dalam tablice visited w algorytmie dijkstry?
teraz jest zmienione.

jest szybsza wersja (kol3a/2022)'''

from zad5testy import runtests
from queue import PriorityQueue

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    edgelist=[[]for _ in range(n)]
    for el in E:
        edgelist[el[0]].append([el[1],el[2]])
        edgelist[el[1]].append([el[0],el[2]])
    for i in range(len(S)):
        for j in range (i+1,len(S)):
            edgelist[S[i]].append([S[j],0])
            edgelist[S[j]].append([S[i],0])
    #visited=[False for _ in range(n)]
    pq=PriorityQueue()
    d=[float("inf") for _ in range(n)]
    d[a]=0
    pq.put((d[a],a))
    u=a
    while not pq.empty():
        _,u=pq.get()
        for v in edgelist[u]:
            if d[v[0]]>d[u]+v[1]:
                d[v[0]]=d[u]+v[1]
                pq.put((d[v[0]],v[0]))
        #visited[u]=True
        #while visited[u]:
         #   if pq.empty(): return None
          #  u=pq.get()[1]
    if d[b]==float('inf'):
        return None
    return d[b]
        
       
            


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
