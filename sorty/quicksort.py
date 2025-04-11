from random import randint
def partition(arr,low,high):
    x=randint(low,high)
    arr[x],arr[high]=arr[high],arr[x]
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def partition_hoare(arr,low,high):
    pi=arr[(high+low)//2]
    i=low-1
    j=high+1
    while True:
        i+=1
        while arr[i]<pi:
            i+=1
        j-=1
        while arr[j]>pi:
            j-=1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]


def quicksort(arr,low,high):
    if low<high:
        pivot_index = partition_hoare(arr,low,high)
        quicksort(arr,low,pivot_index) # w wersji lomuto powinno byc pivot_index-1
        quicksort(arr,pivot_index+1,high)

def qs_bez_rek_ogon(arr,low,high):
    while low<high:
        pivot_index = partition_hoare(arr,low,high)
        qs_bez_rek_ogon(arr,low,pivot_index-1)
        low=pivot_index+1
           
        

arr=[9,4,2,76,42,987,2,-40,2,2,-6,35,8,0,97,1]
quicksort(arr,0,len(arr)-1)
print(arr)