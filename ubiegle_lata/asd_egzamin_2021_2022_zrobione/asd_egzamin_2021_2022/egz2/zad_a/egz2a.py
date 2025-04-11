from egz2atesty import runtests

# zlozonosc akceptowalna 

def coal_n2( A, T ):
    # tu prosze wpisac wlasna implementacje
    magaz=[T]
    for i in range(len(A)):
        nm=0
        while nm<len(magaz) and magaz[nm]<A[i]:
            nm+=1
        if nm==len(magaz):
            magaz.append(T)
        magaz[nm]-=A[i]
    return nm

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal_n2, all_tests = True )
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True)
