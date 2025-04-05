#Dutch National Flag Algorithm

n = int(input("Enter Size: "))
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())

low = 0
high = len(arr) -1
mid = 0

i = 0
while (mid <= high):
    if arr[mid] == 0:
        arr[mid],arr[low] = arr[low],arr[mid]
        low += 1
        mid += 1
        
    elif arr[mid] == 1:
        mid+=1
    
    else:
        arr[mid], arr[high] = arr[high],arr[mid]
        high -=1
        
print(arr)

        
        