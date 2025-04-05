n = int(input("Enter Size: "))
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())

for i in range(len(arr)):
    if arr[i] != i+1:
        if arr[i]-1 < len(arr):
            arr[arr[i]-1],arr[i] = arr[i],arr[arr[i]-1]

for i in range(len(arr)):
    if i+1 != arr[i]:
        print(i+1) 
        break
print(len(arr)+1)

    
