from egz3atesty import runtests

def snow( T, I ):
    A=[]
    for p,k in I:
        A.append((p,1))
        A.append((k+1,-1))
    A.sort()
    res,cnt=0,0
    for i,j in A:
        cnt+=j
        res=max(res,cnt)
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
