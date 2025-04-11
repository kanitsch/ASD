def selsort(A):
    for i in range(len(A)):
        min_val=i
        for j in range(i,len(A)):
            if A[min_val]>A[j]:
                min_val=j
        A[i], A[min_val]=A[min_val],A[i]

def insertionsort(A):
    for i in range(1,len(A)):
        key=A[i]
        j=i-1
        while j>=0 and key<A[j]:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key

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
  
a=[0.382,0.234,0.489,0.753,0.333,0.980,0.599,0.823]
print(bucket_sort(a,selsort))          