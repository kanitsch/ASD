'''Karolina Nitsch
Tworzę tablice maksymalnych odległości do danej komnaty, gdzie d[y][x][0] odpowiada najdłuższej trasie do L[y][x] od góry lub z lewej,
a d[y][x][1] od dołu lub z lewej. Wypełniam ją wartościami -1, co oznacza, że nie można wejść do danej komnaty z podanego kierunku.
Pierwszą kolumnę uzupełniam od razu, bo do każdej z tych komnat można wejść tylko od góry, do momentu aż pojawi się komnata niedostępna '#'.
Poniżej tej komnaty nie da się wejść więc pozostawiam wartości -1. Dodatkowo zapisuję w tablicy vis, które wartości w d są już policzone.
Główna część algorytmu opiera się na funkcji rekurencyjnej, która dla podanych współrzędnych y i x i oblicza najdłuższą trasę z podanego kierunku
do danej komnaty i zapisuje ją w tablicy d[y][x][dir] oraz zaznacza odwiedzenie w tablicy vis. Dla kierunku dir=0 najdłuższa odległość
do d[y][x][0] to maximum z d[y][x-1][0], d[y][x-1][1] oraz d[y-1][0] i jeśli ta wartość jest równa -1 to takie dojście jest niemożliwe i zostawiam d[y][x][0]=-1.
W przeciwnym razie dodaję 1, bo trasa wydłuża się o jedną komnatę. Analogicznie dla kierunku dir=1. Wtedy d[y][x][1]=max(d[y][x-1][0],d[y][x-1][1]), d[y+1][1]).
Przy rekurencyjnym wywoływaniu funkcji, jeśli dana komnata była wcześniej odwiedzona z podanego kierunku (więc odległość do niej jest już policzona) to tylko odczytuje 
wartość z tablicy d. Jeśli nie, to ją oblicza i zapisuje. Przy wyjściu poza tablicę zwraca -1, ponieważ dojście stamtąd jest niemożliwe. 
Szukany wynik to d[n-1][n-1][0] ponieważ do komnaty w prawym dolnym rogu można wejść tylko od góry lub z lewej.
Złożoność obliczeniowa wynosi O(n^2), pamięciowa również O(n^2).
'''


from zad7testy import runtests
        
 
def rek(L,d,n,x,y,dir,vis):
    if x<0 or y<0 or y==n:
        return -1
    if vis[y][x][dir]:
        return d[y][x][dir]
    if L[y][x]=='#':
        vis[y][x]=[True,True]
        return -1
    if dir==0:
        d[y][x][0]=max(rek(L,d,n,x-1,y,0,vis),rek(L,d,n,x-1,y,1,vis),rek(L,d,n,x,y-1,0,vis))
        if d[y][x][0]!=-1:
            d[y][x][0]+=1
    if dir==1:
        d[y][x][1]=max(rek(L,d,n,x-1,y,0,vis),rek(L,d,n,x-1,y,1,vis),rek(L,d,n,x,y+1,1,vis))
        if d[y][x][1]!=-1:
            d[y][x][1]+=1
    vis[y][x][dir]=True
    return d[y][x][dir]

def maze( L ):
    n=len(L)
    d=[[[-1,-1] for _ in range(n)] for _ in range(n)]
    i=0
    vis=[[[False,False] for _ in range(n)] for _ in range(n)]
    while i<n and L[i][0]=='.':
        d[i][0][0]=i
        vis[i][0]=[True,True]
        i+=1
    while i<n:
        vis[i][0]=[True,True]
        i+=1
    return rek(L,d,n,n-1,n-1,0,vis)







# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )

