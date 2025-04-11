from zad1testy import runtests

def partition(A,l,r):
    x=A[r]
    i= l - 1
    for j in range(l, r):
        if A[j]<x:
            i+=1
            A[j],A[i]=A[i],A[j]
    i+=1
    A[r],A[i]=A[i],A[r]
    return i

def quickselect(A, l, r, k):
    if l<=r:
        pivot_index= partition(A, l, r)
        if pivot_index==k:
            return A[pivot_index]
        elif pivot_index<k:
            return quickselect(A, pivot_index + 1, r, k)
        else:
            return quickselect(A, l, pivot_index - 1, k)

def Median(T):
    # tu prosze wpisac wlasna implementacje
    line=[]
    n=len(T)
    for i in range(n):
        for j in range(n):
            line.append(T[i][j])
    quickselect(line, 0, n * n - 1, (len(line) - n) // 2 + n)
    quickselect(line, 0, (len(line) - n) // 2 + n, (len(line) - n) // 2)
    i=0
    y=1
    x=0
    while i<(len(line)-n)//2:
        if y>x:
            T[y][x]=line[i]
            i+=1
            x+=1
        else:
            y+=1
            x=0
    x=0
    while i<(len(line)-n)//2 + n:
        T[x][x]=line[i]
        i+=1
        x+=1
    y=0
    x=1
    while i<len(line):
        if x<n:
            T[y][x]=line[i]
            i+=1
            x+=1
        else:
            y+=1
            x=y+1
    return

runtests( Median ) 
