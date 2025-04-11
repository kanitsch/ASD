#najdluzdszy wspolny podciag
#optymalne mnozenie macierzy
#wydawanie reszty najmniejsza iloscia monet

def knapsack(W,P,B):
    n=len(W)
    F=[[0 for _ in range(B+1)] for _ in range(n)]
    for b in range(W[0],B+1):
        F[0][b]=P[0]
    for i in range(1,n):
        for b in range(B+1):
            F[i][b]=F[i-1][b]
            if b>=W[i]:
                F[i][b]=max(F[i][b],F[i-1][b-W[i]]+P[i])
    return F[n-1][B]

def knapsack2d(W,H,P,B,maxh):
    n=len(W)
    F=[[[0 for _ in range(B+1)] for _ in range(maxh+1)] for _ in range(n)]
    for b in range(W[0],B+1):
        for h in range(H[0],maxh+1):
            F[0][h][b]=P[0]
    for i in range(1,n):
        for h in range(maxh+1):
            for b in range(B+1):
                F[i][h][b]=F[i-1][h][b]
                if h>=H[i] and b>=W[i]:
                    F[i][h][b] = max(F[i][h][b], F[i - 1][h-H[i]][b - W[i]] + P[i])


    return F[n-1][maxh][B]

def knapsack2D(weights,heights,P,W,H): #dynamicznie
    n=len(weights)
    F=[[[0 for _ in range(H+1)] for _ in range(W+1)] for _ in range(n)]
    for w in range(weights[0],W+1):
        for h in range(heights[0],H+1):
            F[0][w][h]=P[0]
    for w in range(W+1):
        for h in range(H+1):
            for i in range(1,n):
                F[i][w][h]=F[i-1][w][h]
                if w-weights[i]>=0 and h-heights[i]>=0 and F[i-1][w-weights[i]][h-heights[i]]+P[i]>F[i][w][h]:
                    F[i][w][h]=F[i-1][w-weights[i]][h-heights[i]]+P[i]
    return F[n-1][W][H]

from random import randint
'''
#testy
P=[1,3,2]
weights=[4,7,6]
heights=[5,6,3]
print(krapsack2d(weights,heights,P,12,8))
print(knapsack2D(weights,heights,P,12,8))
P=[10,13,22,8,21,15]
weights=[2,3,6,4,5,7]
heights=[5,7,6,2,3,4]
print(krapsack2d(weights,heights,P,20,15))
print(knapsack2D(weights,heights,P,20,15))
P=[randint(5,40) for _ in range(15)]
weights=[randint(10,20) for _ in range(15)]
heights=[randint(10,20) for _ in range(15)]
print(krapsack2d(weights,heights,P,100,100))
print(knapsack2D(weights,heights,P,100,100))
'''


def suma_podzbioru(A,T): #zakladam ze w tablicy A nie ma wartosci >=T
    n=len(A)
    dp=[[False for _ in range(T+1)] for _ in range(n)]
    if A[0]<T:
        dp[0][A[0]]=True
    dp[0][0]=True
    for i in range(1,n):
        for t in range(T+1):
            if dp[i-1][t]:
                dp[i][t]=True
            if A[i]<=t and dp[i-1][t-A[i]]:
                dp[i][t]=True
    return dp[n-1][T]

def sumT(A,T): #dynamik v1
    tab=[False for _ in range(T+1)]
    tab[0]=True
    n=len(A)
    for i in range(n):
        for j in range(T,A[i]-1,-1):
            if tab[j-A[i]]: tab[j]=True
    return tab[T]
'''
A=[3,7,7,14,12]
print(sumT(A,28))
'''

# drzewo

# Mamy dane ukorzenione drzewo T
# Każdy wierzchołek ma przypisaną liczbę (być może ujemną)
# Znaleźć najbardziej wartościową ścieżkę (suma wartości węzłów jest jaknajwiększa)


class Node:

    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
        self.maxpath=None


def tree(root):
    maxValue = -float('inf')

    def rek(a):
        nonlocal maxValue
        if a == None:
            return 0
        if a.maxpath:
            return a.maxpath

        childrenMax = [rek(a.children[i]) for i in range(len(a.children))]

        m1 = 0
        m2 = 0
        if len(childrenMax) > 0:
            m1 = max(childrenMax)
            childrenMax.remove(m1)
        if len(childrenMax) > 0:
            m2 = max(childrenMax)
        childrenMax.append(m1)

        maxValue = max(maxValue, a.value + m1 + m2)

        a.maxpath= max(0, a.value + max(childrenMax))
        return a.maxpath

    rek(root)
    return maxValue

'''
v = Node(6)
v.children = [Node(-1), Node(4)]
v.children[1].children = [Node(10),Node(-12)]
v.children[1].children[0].children=[Node(-5)]
print(tree(v))

'''

def najdl_wsp_podc(A,B):
    n=len(A)
    dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            if A[i-1]==B[j-1]:
                dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1)
    return dp[-1][-1]
'''
A=[1,3,5,7,9]
B=[1,2,3,4,5]
print(najdl_wsp_podc(A,B))
A=[1,2,3,4,5,6,7,8,9]
B=[1,2,3,4,5,6,7,8,9]
print(najdl_wsp_podc(A,B))
A=[1,3,5,7,9,11,13,15]
B=[2,4,6,8,10,12,14,16]
print(najdl_wsp_podc(A,B))
A=[9,12,30,23,29,3,4]
B=sorted(A)
print(najdl_wsp_podc(A,B))
'''

def binsearch(tab, value):
    start = 0
    end = len(tab) - 1
    while start <= end:
        middle = (start + end) // 2
        if tab[middle]==value:
            return middle
        if value > tab[ middle ]: start = middle + 1
        else: end = middle - 1
    return start

def lis_nlogn(A):
    n=len(A)
    T=[A[0]]
    for i in range(1,n):
        if A[i]>T[-1]:
            T.append(A[i])
        else:
            idx=binsearch(T,A[i])
            T[idx]=A[i]
    return len(T)

#A=[2,4,3,3,6,1,16]
#print(lis_nlogn(A))


def calc(A,dp,i,j,k):
    if dp[i][j][k]==-1:
        if k>j-i:
            return 0
        dp[i][j][k]=0
        for m in range(k):
            l=k-m-1
            for p in range(i,j):
                dp[i][j][k]=max(dp[i][j][k],min(calc(A,dp,i,p,m),calc(A,dp,p+1,j,l)))
    return dp[i][j][k]

def maximin(A,k):
    n=len(A)
    sums=[0 for _ in range(n+1)]
    for i in range(1,n+1):
        sums[i]=sums[i-1]+A[i-1]
    dp=[[[-1 for _ in range(k)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            dp[i][j][0]=sums[j+1]-sums[i]
    return calc(A,dp,0,n-1,k-1)

#A=[1,2,3,4,8,5]
#print(maximin(A,3))

def wydawanie_monet(M,T):
    f=[float('inf') for _ in range(T+1)]
    f[0]=0
    for i in M:
        for j in range(i,T+1):
            f[j]=min(f[j],j//i+f[j%i])
    return f[-1]
'''
M=[1,5,8]
print(wydawanie_monet(M,6))
'''
def odtworz(S,dp,i,j):
    if i==0 and j==0:
        print((i,j))
        return
    if i-1>=0 and dp[i-1][j]<dp[i][j-1]:
        odtworz(S,dp,i-1,j)
    else:
        odtworz(S,dp,i,j-1)
    print((i,j))
    return


def szachownica(S):
    n=len(S)
    dp=[[float('inf') for _ in range(n)] for _ in range(n)]
    dp[0][0]=S[0][0]
    def uzup(i,j):
        if i<0 or j<0:
            return float('inf')
        if dp[i][j]<float('inf'):
            return dp[i][j]
        dp[i][j]=min(uzup(i-1,j),uzup(i,j-1))+S[i][j]
        return dp[i][j]
    uzup(n-1,n-1)
    print(dp)
    odtworz(S,dp,n-1,n-1)

#S=[[1,2,3,4],[4,4,4,4],[3,1,3,2],[2,2,1,3]]
#szachownica(S)

