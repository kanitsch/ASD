from zad2testy import runtests
'''Karolina Nitsch 421767
Algorytm kopiuje pierwsze p elementów do nowej listy i sortuje je w porządku rosnącym (metodą heapsort), następnie w pętli dodaje do sumy
k-ty element od konca (czyli k-ty największy), usuwa element, który wystąpił najwcześciej w podanej tablicy i wstawia nowy element (kolejny z tablicy).
Znajdowanie indeksu do usunięcia lub wstawienia elementu jest wykonywane za pomocą wyszukiwania binarnego. Po zakończeniu pętli dodaje do sumy k-ty 
największy element z pomocniczej listy, ponieważ ze względu na warunek pętli nie został on dodany po ostatniej modyfikacji listy. 
Złożoność czasowa wynosi O(nlogp), a pamięciowa O(p) '''

def heapify(A,n,i):
    l=2*i+1
    r=2*i+2
    max_ind=i
    if l<n and A[l]>A[max_ind]:
        max_ind=l
    if r<n and A[r]>A[max_ind]:
        max_ind=r
    if max_ind!=i:
        A[i],A[max_ind]=A[max_ind],A[i]
        heapify(A,n,max_ind)

def buildheap(A):
    n=len(A)
    for i in range(n//2,-1,-1):
        heapify(A,n,i)

def heapsort(A):
    n=len(A)
    buildheap(A)
    for i in range(n-1,0,-1):
        A[i],A[0]=A[0],A[i]
        heapify(A,i,0)

def whereToInsert(tab,x):
    left, right = 0, len(tab) - 1
    while left < right:
 
        mid = (left + right) // 2 +1
        if x >= tab[mid-1] and tab[mid]>=x:
            return mid 
        elif x < tab[mid]:
            right = mid -1
        else:
            left = mid +1
    return right if x<tab[right] else right+1

def indexToPop(A,x):
    left=0
    right=len(A)-1
    while left<=right:
        mid=(left+right)//2
        if x==A[mid]:
            return mid
        elif x<A[mid]:
            right=mid-1
        else: left=mid+1
        

def ksum(T, k, p):
    tab=T[:p]
    heapsort(tab)
    #quicksort(tab,0,p-1)
    suma=0
    old=0
    new=p
    while new!=len(T):
        suma+=tab[-k]
        usun=T[old]
        wstaw=T[new]
        #i1=indexToPop(tab,usun)
        i1=indexToPop_rek(tab,0,p-1,usun)
        tab.pop(i1)
        #i2=whereToInsert(tab,wstaw)
        i2=indexToInsert_rek(tab,0,p-1,wstaw)
        tab.insert(i2, wstaw)
        old+=1
        new+=1
    suma+=tab[-k]
    return suma 

def partition(T,p,r):
    x=T[r]
    i=p-1
    for j in range(p,r):
        if T[j]<x:
            i+=1
            T[j],T[i]=T[i],T[j]
    i+=1
    T[r],T[i]=T[i],T[r]
    return i

def qs_logn(T,p,r):
    while p<r:
        q=partition(T,p,r)
        if (q-p)>(r-q):
            qs_logn(T,q+1,r)
            r=q-1
        else:
            qs_logn(T,p,q-1)
            p=q+1
            
def quicksort(arr,low,high):
    if low<high:
        pivot_index = partition(arr,low,high)
        quicksort(arr,low,pivot_index-1)
        quicksort(arr,pivot_index+1,high)


def indexToPop_rek(A, left, right, x):
    mid = (left + right) // 2
    if x == A[mid]:
        return mid
    elif x < A[mid]:
        return indexToPop_rek(A, left, mid - 1, x)
    else:
        return indexToPop_rek(A, mid + 1, right, x)
    
def indexToInsert_rek(A,left,right,x):
    if left==right:
        if right==len(A):
            return right
        return right if x<A[right] else right+1
    mid=(left+right)//2+1
    if x >= A[mid-1] and A[mid]>=x:
            return mid 
    elif x < A[mid]:
        return indexToInsert_rek(A,left,mid-1,x)
    else:
        return indexToInsert_rek(A,mid+1,right,x)
    
    



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
