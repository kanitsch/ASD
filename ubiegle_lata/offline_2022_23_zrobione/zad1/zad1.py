from zad1testy import runtests

def ceasar( s ):
    # tu prosze wpisac wlasna implementacje
    n=len(s)
    maxx=1
    for i in range(1,n-1):
        j=i-1
        k=i+1
        curr_lenth=1
        while j>=0 and k<n:
            if s[j]==s[k]:
                curr_lenth+=2
            else:
                break
            j-=1
            k+=1
        maxx=max(maxx,curr_lenth)

    return maxx

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
