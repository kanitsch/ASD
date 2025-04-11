from zad3testy import runtests

def selsort(A):
    for i in range(len(A)):
        min_val=i
        for j in range(i,len(A)):
            if A[min_val]>A[j]:
                min_val=j
        A[i], A[min_val]=A[min_val],A[i]

def bucket_sort(T,sorting_function):
    n=T[0]
    l=len(T)
    for i in range(l):
        if T[i]>n:
            n=T[i]
    buckets=[[] for _ in range (l+1) ]
    for x in T:
        i=((x/n)*l)
        buckets[int(i)].append(x)
    result=[]
    for bucket in buckets:
        if bucket:
            sorting_function(bucket)
        for x in bucket:
            result.append(x)
    return result


def SortTab(T,P):
    # tu prosze wpisac wlasna implementacje
    return bucket_sort(T,selsort)
    return

runtests( SortTab )