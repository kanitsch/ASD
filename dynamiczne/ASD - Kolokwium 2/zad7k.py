from zad7ktesty import runtests 

# jest po polnocy. problem sprowadza sie do problemu plecakowego z wykladu ale teraz nie rozumiem tego rozwiazania.
# Dziala i przechodzi testy

def policz_korzen(x,y,T):
    if y==len(T) or y<0 or x<0 or x==len(T[0]) or T[y][x]==0:
        return 0
    s=T[y][x]
    T[y][x]=0
    
    if y>0:
        return s+policz_korzen(x+1,y,T)+policz_korzen(x-1,y,T)+policz_korzen(x,y+1,T)+policz_korzen(x,y-1,T)
    else: return s+policz_korzen(x,y+1,T)

    
    
        

def ogrodnik (T, D, Z, l):
    n=len(D)
    korz=[0 for _ in range(n)]
    for i in range(n):
        korz[i]=policz_korzen(D[i],0,T)
    F=[[0 for _ in range(l+1)] for _ in range(n)]
    for b in range(korz[0],l+1):
        F[0][b]=Z[0]
    for b in range(l+1):
        for i in range(1,n):
            F[i][b]=F[i-1][b]
            if b-korz[i]>=0:
                F[i][b]=max(F[i][b],F[i-1][b-korz[i]]+Z[i])

    return F[-1][l]

runtests( ogrodnik, all_tests=True )
