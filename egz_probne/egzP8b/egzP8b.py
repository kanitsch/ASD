from egzP8btesty import runtests

def marshall(S):
    n=len(S)
    for k in range(n):
        for x in range(n):
            for y in range(n):
                S[x][y]=min(S[x][y], S[x][k]+S[k][y])
                #mozna tutaj tez obliczac maciez parentów
                #ostatni wierzcholek przed y na sciezce z x do y: P[x][y]
                #P[x][y]=P[k][y] jezeli zmieniamy odleglosc
    return S

def matrix(G):
    n=len(G)
    M=[[float('inf') for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v,x in G[u]:
            M[u][v]=x
    return M


def robot( G, P ):
    #Tutaj proszę wpisać własną implementację
    M=matrix(G)
    M=marshall(M)
    n=len(P)
    summ=0
    for i in range(n-1):
       u=P[i]
       v=P[i+1]
       summ+=M[u][v] 
    return summ
    
runtests(robot, all_tests = True)
