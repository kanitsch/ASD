from zad2testy import runtests

# uzylam slownikow celowo, mimo ze w zadaniu bylo to zabronione
def counting_less(A):
    n=len(A)
    C={}
    for x,e in A:
        if x in C:
            C[x]+=1
        else:
            C[x]=1
    C_sorted=sorted(C.items())
    for i in range(len(C_sorted)):
        C_sorted[i]=[C_sorted[i][0],C_sorted[i][1]]
    C[C_sorted[0][0]]=0
    for i in range(1,len(C_sorted)):
        C[C_sorted[i][0]]*=-1
        C_sorted[i][1]+=C_sorted[i-1][1]
        C[C_sorted[i][0]]+=C_sorted[i][1]
    return C

def counting_more(A):
    n=len(A)
    C={}
    for x,e in A:
        if e in C:
            C[e]+=1
        else:
            C[e]=1
    C_sorted=sorted(C.items())
    for i in range(len(C_sorted)):
        C_sorted[i]=[C_sorted[i][0],C_sorted[i][1]]
    C[C_sorted[-1][0]]=0
    for i in range(len(C_sorted)-2,-1,-1):
        C[C_sorted[i][0]]*=-1
        C_sorted[i][1]+=C_sorted[i+1][1]
        C[C_sorted[i][0]]+=C_sorted[i][1]
    return C


def depth1(L):  # O(n^2)
    L.sort(key=lambda x: x[0])
    max_ = 0
    n = len(L)
    for i in range(n):
        curr = 0
        for j in range(i + 1, n):
            if L[i][0] <= L[j][0] and L[i][1] >= L[j][1]:
                curr += 1
        max_ = max(max_, curr)

    return max_
def depth(L):
    # tu prosze wpisac wlasna implementacje
    n=len(L)
    maxstart=0
    maxend=0
    for s,e in L:
        maxstart=max(maxstart,s)
        maxend=max(maxend,e)
    cl=counting_less(L)
    cm=counting_more(L)
    maxdepth=0
    for s,e in L:
        depth=n-cl[s]-cm[e]-1
        maxdepth=max(maxdepth,depth)
    return maxdepth


runtests( depth )
