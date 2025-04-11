from zad1testy import runtests

#bedzie O(n^2) bo tak bylo na wykladzie i mi sie juz nie chce

def malejacy_podc(X):
    n=len(X)
    F=[1 for _ in range(n)]
    for i in range(n):
        maxx=0
        for j in range(i):
            if X[j]>X[i]:
                maxx=max(maxx,F[j])
        F[i]=maxx+1
    return F



def mr( X ):
    """tu prosze wpisac wlasna implementacje"""
    n=len(X)
    X_rev=X[::-1]
    rosn=malejacy_podc(X_rev)
    rosn.reverse()
    #print(rosn)
    mal=malejacy_podc(X)
    best=rosn[0]
    ind=-1
    ind1=0
    for i in range(1,n-1):
        for j in range(i+1,n):
            if rosn[j]+mal[i]>best and X[i]!=X[j]:
                best=rosn[j]+mal[i]
                ind=i
                ind1=j
    if mal[-1]>best:
        best=mal[-1]
        ind=n-1
        res=[X[-1]]
    elif ind==-1:
        res=[X[0]]
    else:
        res=[X[ind],X[ind1]]
    j=ind
    for i in range(ind,-1,-1):
        if X[i]>X[j] and mal[i]==mal[j]-1:
            res.insert(0,X[i])
            j=i
    j=ind1
    for i in range(ind1,n):
        if X[i]>X[j] and rosn[i]==rosn[j]-1:
            res.append(X[i])
            j=i
    
    return res

    

runtests(mr)




