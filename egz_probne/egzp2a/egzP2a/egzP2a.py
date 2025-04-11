from egzP2atesty import runtests 


def indeksowanie(m,k,n):
    start=[0 for _ in range(m)]
    end=[0 for _ in range(m)]
    act_width=m+k-1
    act_start=0
    act_end=-1
    for i in range(m):
        act_start=act_end+1
        start[i]=act_start
        act_end=start[i]+act_width-1
        end[i]=act_end
        act_width-=1
    new_ind=0
    col=0
    row=0
    indices=[0 for _ in range(n)]
    while new_ind<n:
        if start[row]+col<=end[row]:
            indices[start[row]+col]=new_ind
            new_ind+=1
        row+=1
        if row==m:
            row=0
            col+=1
    return indices,end
 
def partition(arr,left,right,ind):
    x=arr[ind[right]][1]
    i=left-1
    for j in range(left,right):
        if arr[ind[j]][1]>x:
            i+=1
            arr[ind[j]],arr[ind[i]]=arr[ind[i]],arr[ind[j]]
    i+=1
    arr[ind[right]],arr[ind[i]]=arr[ind[i]],arr[ind[right]]
    return i

def quickselect(arr,ind, left, right, k):
    if left<=right:
        pivot_index=partition(arr,left,right,ind)
        if pivot_index>k:
            quickselect(arr,ind,pivot_index + 1, right, k)
        elif pivot_index<k:
            quickselect(arr,ind, left, pivot_index - 1, k)
        return
    
def quicksort(arr,low,high,ind):
    if low<high:
        pivot_index = partition(arr,low,high,ind)
        quicksort(arr,low,pivot_index-1,ind)
        quicksort(arr,pivot_index+1,high,ind)


def zdjecie(T, m, k):
    #tutaj proszę wpisać własną implementację
    n=len(T)
    ind,end=indeksowanie(m,k,n)
    #start=0
    quicksort(T,0,n-1,ind)


               
    
    
    return None

T = [ (1001, 154),(1002, 176),(1003, 189),(1004, 165),(1005, 162),(9293,178),(8765,234),(3744,283),(8374,145),(3245,456)]
zdjecie(T,4,1)
runtests ( zdjecie, all_tests=True )