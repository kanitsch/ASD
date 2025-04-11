from zad5ktesty import runtests


def garek ( A ):
    n=len(A)
    f=[[-1 for _ in range(n)] for _ in range(n)]
    def rek(p,k):
        if f[p][k]!=-1:
            return f[p][k]
        elif p==k:
            f[p][k]=A[p]
        elif p==k-1:
            f[p][k]=max(A[p:k+1])
        else:
            f[p][k]=max(A[p]+min(rek(p+2,k),rek(p+1,k-1)),A[k]+min(rek(p,k-2),rek(p+1,k-1)))
        return f[p][k]
    return rek(0,n-1)

runtests ( garek )