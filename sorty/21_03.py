'''
1) sortowanie zakres 0-n^2
2)
3)czy 2 podane słowa to anagramy
4)
numpy.zeros(n) -inicjalizuje tablice wypełnioną zerami
numpy.empty(n) - -||- pusta tablice
def allocate(n)
5) tablica, wartosci parami różne, max odl między sąsiednimi elementami w posortowanej tablicy'''
'''robimy n bucketów i jezeli są jakieś puste to porównójemy odległości pomiędzy elementami z bucketów sąsiadujących z obu stron z pustymi, jesli nie to liniowo'''
def allocate(n):
    return

def anagram(A,B,n,k):
    costam=[0 for _ in range(k)]
    for i in range(n):
        costam[A[i]]-=1
        costam[B[i]]+=1
    flag=True
    for i in costam:
        if i!=0:
            flag=False
    return flag

def anagram2(A,B,k):
    if len(A)!=len(B):
        return False
    n=len(A)
    C=[0 for _ in range(k)]
    for i in range(n):
        C[ord(A[i])-ord('a')]+=1
        C[ord(B[i])-ord('a')]-=1
    for i in range(n):
        if C[ord(A[i])-ord('a')]!=0:
            return False
    return True

print(anagram2('tok','kot',26))
def count_sort(A,n,key):
    t=[0 for _ in range(n)]
    for i in range(n):
        if key(A[i])>=n:
            print(key(A[i]))
        else:
            t[key(A[i])]+=1
    for i in range(1,n):
        t[i]+=t[i-1]
    A_Z=[0 for _ in range(n)]
    for i in range(len(A)-1,-1,-1):
        A_Z[t[key(A[i])]-1]=A[i]
        t[key(A[i])]-=1
    return A_Z

def radix_sort(A,n):
    A_Z=count_sort(A,n,lambda x: x%n)
    A_Z=count_sort(A_Z,n,lambda x: x//n)
    return A_Z

def unique_vals(A,n):
    vals=[]
    for x in A:
        if not binary_search2(vals,x): #O(n*loglogn)
            #insert(vals,x) #O(log^2(n))
            print('dua')
        return vals
    
def countsort_uniquevals(A,n):
    vals=unique_vals(A,n)
    counters=[0 for _ in range(len(vals))]
    for x in A:
        idx=binary_search2(vals,x)
        counters[idx]+=1
    for i in range(1,len(counters)):
        counters[i]+=counters[i-1]

def minmax(T):
    n=len(T)
    cnt=0
    mini=T[0]
    maxi=T[0]
    if n%2==0:
        start=0
    else:
        start=1
    for i in range(start,n,2):
        if T[i]<T[i+1]:
            mi,ma=T[i],T[i+1]
        else:
            mi, ma=T[i+1],T[i]
        mini=min(mini,mi)
        maxi=max(maxi,ma)
        cnt+=3
    print(mini,maxi,n,cnt)


T=[2,5,32,45,2,14,53,23,65,43,432,2,45,55,42,89,689,54,7,95,332,566,5542,78,97,46]
minmax(T)
tab=[1,2,4,5,6,77,357]
    
t=[890,485,322,356,434,222,456,82,45,678]
minmax(t)
minmax(tab)

def binary_search2(tab, value):
    start = 0
    end = len(tab) - 1
    while start <= end:
        middle = (start + end) // 2
        if value > tab[middle]:
            start = middle + 1
        else:
            end = middle - 1
    if start < len(tab) and tab[start] == value:
        return start
    return -1

def find_sum(A,s):
    n=len(A)
    i=0
    j=n-1
    while i!=j:
        if A[i]+A[j]>s:
            j-=1
        elif A[i]+A[j]<s:
            i+=1
        else:
            return i, j
    return False

A=[1,2,4,6,14,25,67,74,32,10]
print(find_sum(A,29))

print(radix_sort(A,10))


def buckety(T):
    n=T[0]
    m=T[0]
    l=len(T)
    for i in range(l):
        if T[i]>n:
            n=T[i]
        m=min(m,T[i])
    buckets=[[] for _ in range (l+1) ]
    for x in T:
        i=(((x-m)/(n-m))*l)
        buckets[int(i)].append(x)
    return buckets

def maxrozn(T):
    buckets=buckety(T)
    n=len(T)
    i=1
    maxstart=-1
    maxend=-1
    while i<n+1:
        start=i-1
        while i<n and not buckets[i]:
            i+=1
        end=i
        if end-start>maxend-maxstart:
            maxend=end
            maxstart=start
        i+=1
    if maxend-maxstart>1:
        return min(buckets[maxend])-max(buckets[maxstart])
    else:
        res=0
        for i in range(1,n+1):
            res=max(res,buckets[i][0]-buckets[i-1][0])
        return res

T=[3,5,4,2,6,8,10,9]
print(maxrozn(T))

def kolory(A,k):
    n=len(A)
    counters=[0 for _ in range(k)]
    colors=0
    i=0
    j=0
    while colors<k:
        if counters[A[j]]==0:
            colors+=1
        counters[A[j]]+=1
        j+=1
    best=0,j-1
    while j<n:
        while True:
            counters[A[i]]-=1
            if counters[A[i]]==0:
                break
            i+=1
        if j-1-i<best[1]-best[0]:
            best=i,j-1
        while j<n and A[j]!=A[i]:
            counters[A[j]]+=1
            j+=1
        if j<n and A[j]==A[i]:
            if j - i < best[1] - best[0]:
                best = i+1, j
            counters[A[j]]=1
            j+=1
            i+=1
    return best

A=[0,1,3,2,3,2,1,4,0,1,3,2,1,3,1,4,0]
print(kolory(A,5))


