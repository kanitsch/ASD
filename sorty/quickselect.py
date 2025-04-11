def partition(arr,left,right):
    x=arr[right]
    i=left-1
    for j in range(left,right):
        if arr[j]>x:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    i+=1
    arr[right],arr[i]=arr[i],arr[right]
    return i

def partition_cw(t,p,q): #nie dziala
    while p<q:
        if t[p]>t[q]:
            if t[p]>t[q]:
                t[p],t[q]=t[q],t[p]
                p+=1
            else:
                q-=1
    return p 

def quickselect(arr, left, right, k):
    if left<=right:
        pivot_index=partition(arr,left,right)
        if pivot_index==k:
            return arr[pivot_index]
        elif pivot_index<k:
            return quickselect(arr,pivot_index + 1, right, k)
        else:
            return quickselect(arr, left, pivot_index - 1, k)
        
t=[4,7,6,23,67,3,0,2,45]
print(quickselect(t,0,len(t)-1,2))
print(t)