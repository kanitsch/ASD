#dla gęstych grafóww
#0(V^3)

def floyd_warshall_marshall(S):
    n=len(S)
    for k in range(n):
        for x in range(n):
            for y in range(n):
                S[x][y]=min(S[x][y], S[x][k]+S[k][y])
                #mozna tutaj tez obliczac maciez parentów
                #ostatni wierzcholek przed y na sciezce z x do y: P[x][y]
                #P[x][y]=P[k][y] jezeli zmieniamy odleglosc
    return S