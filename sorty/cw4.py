def counting_sort(A):
    n=len(A)
    T=[]
    for x in A:
        czy,i=binary_search2(T,x) #nloglogn
        if czy:
            T[i][1]+=1
        else:
            T.insert(i,[x,1])
    ind=0
    for i in range(len(T)): #n
        for j in range(T[i][1]):
            A[ind]=T[i][0]
            ind+=1
    return A

def binary_search2(tab, value):
    start = 0
    end = len(tab) - 1
    while start <= end:
        middle = (start + end) // 2
        if value==tab[middle][0]:
            return True, middle
        if value > tab[ middle ][0]: start = middle + 1
        else: end = middle - 1
    return False, start

def sort_fast(A):
    A=counting_sort(A)
    return A

A=[2,5,37,356,32,82,37,3,37,32,2,2,5,37,82,3,3,3,5]
print(sort_fast(A))