from kol1btesty import runtests

def counting_sort(A):
    n=len(A)
    k=ord('z')-ord('a')
    B=[None for _ in range(n)]
    C=[0 for _ in range(k+1)]
    for x in A:
        C[ord(x)-ord('a')]+=1
    for i in range(1,k+1):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[ord(A[i])-ord('a')]-1]=A[i]
        C[ord(A[i])-ord('a')]-=1
    s=''
    for x in B:
            s+=x
    return s

#print(counting_sort('tygrysz'))

def cs_in_bucket(A,no):
    n=len(A)
    k=ord('z')-ord('a')
    B=[None for _ in range(n)]
    C=[0 for _ in range(k+1)]
    for x in A:
        C[ord(x[no])-ord('a')]+=1
    for i in range(1,k+1):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[ord(A[i][no])-ord('a')]-1]=A[i]
        C[ord(A[i][no])-ord('a')]-=1
    return B

def f(T):
    # tu prosze wpisac wlasna implementacje
    maxlen=0
    for i in range(len(T)):
        T[i]=counting_sort(T[i])
        maxlen=max(maxlen,len(T[i]))
    buckets=[[] for _ in range(maxlen+1)]
    n=len(T)
    for i in range(len(T)):
        buckets[len(T[i])].append(T[i])
    maxx=1
    for i in range(1,maxlen+1):
        if len(buckets[i])<=maxx:
            continue
        for j in range(i-1,-1,-1):
            buckets[i]=cs_in_bucket(buckets[i],j)
        cnt=1
        for j in range(1,len(buckets[i])):
            if buckets[i][j]!=buckets[i][j-1]:
                maxx=max(maxx,cnt)
                cnt=1
            else:
                cnt+=1
        maxx=max(maxx,cnt)  
    return maxx 
                
    
        
        
    


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True)

