from math import log10
def countingsort(A,divisor):
    counter_length=10
    n=len(A)
    counter=[0 for _ in range(counter_length)]
    for num in A:
        counter[(num//divisor)%10]+=1
    for i in range(1,counter_length):
        counter[i]+=counter[i-1]
    output=[0 for _ in range(counter_length)]
    for i in range(n-1,-1,-1):
        output[counter[(A[i]//divisor)%10]-1] = A[i]
        counter[(A[i]//divisor)%10]-=1
    return output

def radixsort(A):
    k=int(log10(max(A)))+1
    for i in range(k):
        A=countingsort(A,10**i)
    return A

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
        
A=[837,291,666,339,0,988,78,543,97,100]
A=bubblesort(A)
print(A)

