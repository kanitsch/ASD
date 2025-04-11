from egzP6atesty import runtests 

#akceptowalna

def mergesort(A,wsp):
    n=len(A)
    if n==1:
        return A
    a1=A[:n//2]
    a2=A[n//2:]
    a1=mergesort(a1,wsp)
    a2=mergesort(a2,wsp)
    return merge(a1,a2,wsp)
    
    
def merge(a1,a2,wsp):
    i=j=0
    x=0
    n=len(a1)+len(a2)
    A=[0 for _ in range(n)]
    while i < n//2 and j < len(a2):
        if a1[i][wsp]<a2[j][wsp]:
            A[x]=a1[i]
            i+=1
        else:
            A[x]=a2[j]
            j+=1
        x+=1
    while i<len(a1):
        A[x]=a1[i]
        x+=1
        i+=1
    while j<len(a2):
        A[x]=a2[j]
        x+=1
        j+=1
    return A

def modify(H):
    n=len(H)
    newH=[]
    for i in range(n):
        cnt=0
        for j in range(len(H[i])):
            if ord('0')<=ord(str(H[i][j]))<=ord('9'):
               cnt+=1 
        newH.append((H[i],len(H[i]),cnt))
    return newH

def google ( H, s ):
    #tutaj proszę wpisać własną implementację
    #print(s)
    A=modify(H) 
    A=mergesort(A,2)
    A=mergesort(A,1)
    A.reverse()
    return A[s-1][0]


runtests ( google, all_tests=True )

