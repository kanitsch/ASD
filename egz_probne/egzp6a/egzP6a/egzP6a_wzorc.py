from egzP6atesty import runtests 

def partition(A,p,r):
    x=A[r][1]
    i=p-1
    for j in range(p,r):
        if A[j][1]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
        A[i+1],A[r]=A[r],A[i+1]
    return i+1

def select(A,p,r,k):
    if p==r:
        return A[p]
    q=partition(A,p,r)
    if q==k: return A[q]
    elif k<q:
        return select(A,p,q-1,k)
    else:
        return select(A,q+1,r,k)
    
def ilecyfr(s):
    n=len(s)
    cnt=0
    for ch in s:
        if '0'<=ch<='9':
            cnt+=1
    return cnt
            

def google ( H, s ):
    maxlen=0
    for stri in H:
        maxlen=max(maxlen,len(stri))
    T=[[] for _ in range(maxlen+1)]
    for stri in H:
        T[len(stri)].append(stri)
    i=maxlen
    while len(T[i])<s:
        s-=len(T[i])
        i-=1
    T=T[i]
    '''for j in range(len(T)):
        T[j]=(T[j],ileliter(T[j]))
        
    yyy=select(T,0,len(T)-1,s-1)
    return yyy[0]'''
    maxx=0
    for j in T:
        maxx=max(maxx,ilecyfr(j))
    buckets=[[] for _ in range(maxx+1)]
    for j in T:
        ile=ilecyfr(j)
        buckets[ile].append(j)
    #print(buckets)
    x=0
    while len(buckets[x])<s:
        s-=len(buckets[x])
        x+=1
    while not buckets[x]:
        x+=1
    return buckets[x][0]
        
        
    
    


runtests ( google, all_tests=True )

