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
t=[2,4,5,3,6,5,4,3,2]
print(counting_sort(t,7))