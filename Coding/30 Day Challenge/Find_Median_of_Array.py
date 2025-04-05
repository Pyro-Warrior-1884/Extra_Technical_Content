import random

def partition(arr,low,high):
    print(low,high)
    pivot = arr[high]
    i=low-1
    for j in range(low,high):
        print(arr)
        if arr[j] <=  pivot:
            print(i)
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
            

def random_partition(arr,low,high,k):
    random_index = random.randint(low,high)
    arr[random_index], arr[high] = arr[high],arr[random_index]
    return partition(arr,low,high)


def quicksort(arr,low,high,k):
    if low <= high:
        pivot_index = random_partition(arr,low,high,k)
        
        if pivot_index == k:
            return arr[pivot_index]        
        elif pivot_index < k:
            return quicksort(arr, pivot_index+1 , high, k)            
        else:
            return quicksort(arr, low, pivot_index-1, k)
    return

arr = [3,2,1,4,5,7,8,6,10,9]
k = (len(arr)//2) +1

if len(arr)%2 != 0:  
    k = len(arr) - k      
    result = quicksort(arr,0,len(arr)-1,k)
else:
    k = len(arr) - k
    result = (quicksort(arr,0,len(arr)-1,k) + quicksort(arr,0,len(arr)-1,k+1))/2
print("Average of the Array: ",result)

    