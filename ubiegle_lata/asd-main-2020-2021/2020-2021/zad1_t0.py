from zad1_t0_testy import runtests

def counting_sort(A,k):
    n=len(A)
    B=[None for _ in range(n)]
    C=[0 for _ in range(k)]
    for x in A:
        C[x[0]]+=1
    for i in range(1,k):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i][0]]-1]=A[i]
        C[A[i][0]]-=1
    return B

def tanagram_n2(x,y,t):
    n=len(x)
    if n!=len(y):
        return False
    tab=[False for _ in range(n)]
    for i in range(n):
        flag=False
        for j in range(max(i-t,0),min(i+t+1,n)):
            if x[i]==y[j] and not tab[j]:
                tab[j]=True
                flag=True
                break
        if not flag:
            return False
        
    return True

def tanagram(x,y,t):
    if len(x)!=len(y):
        return False
    n=len(x)
    A=[0 for _ in range(n)]
    B=[0 for _ in range(n)]
    for i in range(n):
        A[i]=[ord(x[i])-ord('a'),i]
        B[i]=[ord(y[i])-ord('a'),i]
    A=counting_sort(A,26)
    B=counting_sort(B,26)
    for i in range(n):
        if abs(A[i][1]-B[i][1])>t:
            return False
    return True


x='kotomysz'
y='tokmysoz'
print(tanagram(x,y,3))
print(tanagram(x,y,2))

runtests(tanagram)