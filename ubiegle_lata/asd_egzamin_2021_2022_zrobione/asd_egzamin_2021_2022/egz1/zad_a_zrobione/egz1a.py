from egz1atesty import runtests

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]>=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

        
def quicksort(arr,low,high):
    if low<high:
        pivot_index = partition(arr,low,high)
        quicksort(arr,low,pivot_index-1)
        quicksort(arr,pivot_index+1,high)

def snow( S ):
    # tu prosze wpisac wlasna implementacje
    quicksort(S,0,len(S)-1)    
    i=0
    day=0
    suma=0
    while S[i]-day>0:
        suma+=S[i]-day
        i+=1
        day+=1
    return suma

def counting_sort(A,k):
    n=len(A)
    B=[None for _ in range(n)]
    C=[0 for _ in range(k)]
    for x in A:
        C[x]+=1
    for i in range(1,k):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]-=1
    return B

def snow_n(S):
    day=0
    n=len(S)
    suma=0
    for i in range(n):
        if S[i]>=n:
            suma+=S[i]-day
            day+=1
            S[i]=0
    S=counting_sort(S,n)
    S.reverse()
    i=0
    while S[i]-day>0:
        suma+=S[i]-day
        day+=1
        i+=1
    return suma




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow_n, all_tests = True )
