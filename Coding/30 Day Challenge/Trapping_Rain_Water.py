arr_size = int(input("Entter Size: "))
arr = [0 for _ in range(arr_size)]
for i in range(arr_size):
    arr[i] = int(input())

left = [0 for _ in range(len(arr))]
right = [0 for _ in range(len(arr))]

max = 0
for i in range(len(arr)):
    if max < arr[i]:
        max = arr[i]
    left[i] = max
    
max = 0    
for i in range(len(arr)-1,-1,-1):
    if max < arr[i]:
        max = arr[i]
    right[i] = max

water_collected = 0
for i in range(len(arr)):
    water_collected += min(left[i],right[i]) - arr[i]

print(water_collected)



    