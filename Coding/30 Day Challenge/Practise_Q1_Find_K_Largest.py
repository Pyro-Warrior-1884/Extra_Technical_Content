import random

def partition(arr,low,high): #the main place where they place the pivot and then places all the lesser elements to the left of the pivot 
    pivot = arr[high] 
    i = low-1 
    
    for j in range(low,high):   
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    
    
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def randomized_partition(arr,low,high,k):#makes the random pivot places it at the end and send to partition 
    random_index = random.randint(low, high)
    arr[random_index],arr[high] = arr[high],arr[random_index] 
    return partition(arr,low,high)

def quickselect(arr,low,high,k):#finds a pivot randomly and places it at the position of index which shows its position as the smallest in the array
    if low <= high:
        pivot_index = randomized_partition(arr, low, high, k)
       
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return quickselect(arr, low, pivot_index-1, k)
        else:
            return quickselect(arr, pivot_index+1, high, k)
    return   

def find_K_largest(arr,k):
    k = len(arr) - k 
    return quickselect(arr,0,len(arr)-1,k) 

arr = [3, 2, 1, 5, 6, 4]
k = 1
result = find_K_largest(arr,k) 
print(f"The {k}th Largest Element: ",result)
