from egz2btesty import runtests

def magic( C ):
    # tu prosze wpisac wlasna implementacje
    n=len(C)
    t=[-1 for _ in range(n)]
    t[0]=0
    for i in range(n-1):
        if t[i]!=-1:
            skrzynia=C[i][0]
            for j in range(1,4):
                k,w=C[i][j]
                if w>i:
                    wez=skrzynia-k
                    if -t[i]<=wez<=10:
                        if t[w]<t[i]+wez:
                            t[w]=t[i]+wez
                
    return t[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
