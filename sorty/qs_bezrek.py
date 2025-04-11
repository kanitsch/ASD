def qs_iter(t):
    n=len(t)
    stack=[(0,n-1)]
    while len(stack)>0:
        l,r=stack.pop()
        if l<=r:
            p=partition(t,l,r)
            stack.extend([(l,p-1),(p+1,r)])

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

t=[3,6,5,4,8,1]
qs_iter(t)
print(t)