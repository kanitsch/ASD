from zad3testy import runtests

def selsort(A):
    for i in range(len(A)):
        min_val=i
        for j in range(i,len(A)):
            if A[min_val]>A[j]:
                min_val=j
        A[i], A[min_val]=A[min_val],A[i]

def bubblesort(A):
    n=len(A)
    for i in range(n):
        sorted=True
        for j in range(n-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
                sorted=False
        if sorted:
            break
    return A

def bucket_sort(T,sorting_function):
    n=max(T)
    l=len(T)
    buckets=[[] for _ in range (l+1) ]
    for x in T:
        i=((x/n)*l)
        buckets[int(i)].append(x)
    i=0
    for bucket in buckets:
        if bucket:
            sorting_function(bucket)
        for x in bucket:
            T[i]=x
            i+=1
    return
def SortTab(T,P):
    # tu prosze wpisac wlasna implementacje
    bucket_sort(T,bubblesort)
    return

runtests( SortTab )