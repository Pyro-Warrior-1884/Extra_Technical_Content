
n = int(input("Enter Size of Arr1: "))
arr1 = [0 for _ in range(n)]
for i in range(n):
    arr1[i] = int(input())
    
n = int(input("Enter Size of Arr2: "))
arr2 = [0 for _ in range(n)]
for i in range(n):
    arr2[i] = int(input())
    
m = len(arr1)
n = len(arr2)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low+1, high+1):
        if arr[j] < pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Place pivot in the correct position
    return i - 1

def in_place_quick(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        in_place_quick(arr, low, pi-1)
        in_place_quick(arr, pi+1, high)
        
arr1.extend(arr2)
in_place_quick(arr1, 0, len(arr1)-1)
for i in range(n):
    arr2[i] = arr1[m+i]
for i in range(n-1,-1,-1):
    arr1.remove(arr1[m+i])
    
print("arr1 = ",arr1,"arr2 = ",arr2)

    

    

    