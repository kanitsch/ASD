from egzP5atesty import runtests 

#akceptowalna?

def inwestor ( T ):
    maxx=0
    n=len(T)
    for i in range(n):
        minn=float('inf')
        for j in range(i,n):
            minn=min(minn,T[j])
            maxx=max(maxx,minn*(j-i+1))


    return maxx

def inwestor_lepszy(T):
    n=len(T)
    l=[-1 for _ in range(n)]
    p=[n for _ in range(n)]
    stos=[]
    stos.append(-1)
    stos.append(0)
    for i in range(1,n):
        while stos:
            j=stos.pop()
            if T[j]<T[i]:
                l[i]=j
                stos.append(j)
                break
            elif T[j]==T[i]:
                l[i]=l[j]
                stos.append(j)
                break
            else:
                p[j]=i
        stos.append(i)
    maxx=0
    for i in range(n):
        maxx=max(maxx,T[i]*(p[i]-l[i]-1))
    return maxx



runtests ( inwestor_lepszy, all_tests=True )