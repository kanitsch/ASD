

T1 = [1, 8, 3, 4, 5, 1, 2]
T2= [1, 8, 3, 4, 5, 2, 0, 0, 0, 0]
T3= [1, 0, 8, 0, 3, 0, 4, 0, 5, 0, 2]
T4 = [8, 12, 3, 4, 7, 1, 2, 10]
T = [8, 1, 3, 4, 5, 1, 2]
#print(forrest(T1))


def blackf(C):
    n=len(C)
    F=[[0,0]for _ in range(n)]
    F[0][1]=C[0]
    F[1][0]=C[0]
    F[1][1]=C[1]
    for i in range(1,n):
        F[i][0]=F[i-1][1]
        F[i][1]=max(F[i-1][0]+C[i],F[i-1][1])
    A=[]
    i=n-1
    while i>=0:
        if F[i][1]>F[i][0]:
            A.append(i)
            i-=2
        else:
            i-=1
    A.reverse()
    return F[n-1][1],A

def czarnylas(C):
    n=len(C)
    F=[0 for _ in range(n)]
    F[0]=C[0]
    F[1]=max(C[0],C[1])
    for i in range(2,n):
        F[i]=max(F[i-1],F[i-2]+C[i])
    i=n-1
    res=[]
    while i-1>=0:
        while i-1>=0 and F[i-1]==F[i]:
            i-=1
        res.append(i)
        i-=2
    if i==0:
        res.append(0)
    res.reverse()
    return F[-1],res


print(blackf(T4))
print(czarnylas(T4))


def zaba_u(A):
    n = len(A)
    F = [[float('inf')] * n for _ in range(n)]
    for j in range(n):
        F[j][0] = 0
    for i in range(1, A[0]):
        F[min(i, n - 1)][min(A[0] - i, n - 1)] = 1
    print(F)
    for i in range(n):
        for j in range(1, n):
            if F[i][j] < float('inf'):
                energy = min(A[j] + i, n - 1 - j)
                for k in range(energy):
                    next_j = j + energy - k
                    print("SKOK z", i, j, "do", k, next_j)
                    F[k][next_j] = min(F[k][next_j], F[i][j] + 1)
    return min(F[i][n - 1] for i in range(n))
    # return F[0][n - 1]


def zaba(A):
    n = len(A)
    F = [[float('inf')] * n for _ in range(n)]
    for j in range(n):
        F[j][0] = 0
    for i in range(A[0]):
        F[min(i, n - 1)][min(A[0] - i, n - 1)] = 1
    for i in range(n):
        for j in range(1, n):
            if F[i][j] < float('inf'):
                energy = min(A[j] + i, n - 1 - j)
                for k in range(energy):
                    next_j = j + energy - k
                    F[k][next_j] = min(F[k][next_j], F[i][j] + 1)
    # return min(F[i][n - 1] for i in range(n))
    return F[0][n - 1]

def zbychu(A):
    n=len(A)
    F=[[float('inf') for _ in range(n)] for _ in range(n)]
    for j in range(n):
        F[0][j] = 0
    m=min(A[0],n)
    for i in range(m+1):
        F[i][m-i]=1
    for i in range(1,n):
        for j in range(n):
            if F[i][j]!=float('inf'):
                e=min(j+A[i],n-1-i)
                for k in range(1,e+1):
                    #if e-k<0:
                     #   break
                    F[i+k][e-k]=min(F[i][j]+1,F[i+k][e-k])

    return min(F[n-1])


A = [2, 2, 5, 0, 0,0,3, 0,2,0,0,0,0]
print(zbychu(A))
print(zaba(A))

def klocki(A):
    n=len(A)
    F=[0 for _ in range(n)]
    F[0]=1
    T=[]
    for i in range(1,n):
        for j in range(i):
            if A[i][0]>=A[j][0] and A[i][1]<=A[j][1]:
                F[i]=max(F[i],F[j])
        F[i]+=1
    return  n-max(F)


def binsearch(A, x, p):
    n = len(A)
    i = 0
    j = n - 1
    while i <= j:
        q = (i + j) // 2
        if A[q][p]<=x:
            i = q + 1
        else:
            j = q - 1
    return i


def lis(A, p):
    n = len(A)
    F = []
    for i in range(n):
        a = binsearch(F, A[i][p], p)
        if a == len(F):
            F.append(A[i])
        else:
            F[a] = A[i]
    return F


def klocki2(A):
    F = lis(A, 0)
    F2 = F[::-1]
    F3 = lis(F2, 1)

    return len(A) - len(F3)

#testy
'''
A=[(1,6),(2,8),(2.5,5),(9,12),(3.5,4.5)]
print(klocki2(A))
print(klocki(A))
A=[(1,12),(2,11),(3,10),(4,9),(5,8),(6,7)]
print(klocki2(A))
print(klocki(A))
from random import randint
A=[(randint(2*i,100),randint(101,201-2*i)) for i in range(50)]
print(klocki2(A))
print(klocki(A))
'''
A = [
    [0, 5],
    [1, 4],
    [-3, 7],
    [2, 3],
    [2, 6],
    [4, 6],
    [2, 3]
]

#print(klocki2(A))
#print(klocki(A))

def binary_search2(tab, value):
    _start = 0
    _end = len( tab ) - 1
    while _start <= _end:
        middle = ( _start + _end ) // 2
        if value > tab[ middle ][0]: _start = middle + 1
        else: _end = middle - 1
    if _start < len(tab) and tab[ _start ][0] == value:
        return _start
    return -1

def sklejanie(P,a,b):
    n=len(P)
    f=[None for _ in range(n)]
    P.sort()
    def rek(i):
        if f[i]!=None:
            return f[i]
        if P[i][1]==b:
            f[i]=True
            return True
        x=binary_search2(P,P[i][1])
        if x==-1:
            f[i]=False
            return f[i]
        f[i]=False
        while x<n and P[x][0]==P[i][1]:
            if rek(x):
                f[i]=True
            x+=1
        return f[i]
    i=binary_search2(P,a)
    while i<n and P[i][0]==a:
        if rek(i):
            return True
        i+=1
    return False

def sklejanie2(P,a,b):
    n=len(P)
    f=[-1 for _ in range(n)]
    P.sort()
    def rek(i):
        if f[i]!=-1:
            return f[i]
        if P[i][1]==b:
            f[i]=P[i][2]
            return f[i]
        x=binary_search2(P,P[i][1])
        if x==-1:
            f[i]=float('inf')
            return f[i]
        f[i]=float('inf')
        while x<n and P[x][0]==P[i][1]:
            f[i]=min(f[i],rek(x))
            x+=1
        f[i]+=P[i][2]
        return f[i]
    i=binary_search2(P,a)
    best=float('inf')
    while i<n and P[i][0]==a:
        best=min(best,rek(i))
        i+=1
    return best

P=[(1, 3,10), (1, 4,20),  (3, 6,10), (4, 7,5), (7, 8,10), (6, 9,20), (7, 10,3), (8, 9,2), (9, 12,8)]
print(sklejanie2(P,1,9))




