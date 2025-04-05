n = int(input("Enter Size: "))
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())

check_sum = 0
for i in range(len(arr)-1):
    check_sum += (i+1)

arr_sum = 0
for i in range(len(arr)):
    arr_sum += arr[i] 
    
dup = arr_sum - check_sum
print(dup)