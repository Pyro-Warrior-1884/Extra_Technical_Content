arr = [100, 50, 20, 10]



max_num = arr[len(arr)-1]
leader = []
leader.insert(0, max_num)
for i in range(len(arr)-2,-1,-1):
    if max_num < arr[i]:
        max_num = arr[i]
        leader.insert(0, arr[i])
print(leader)

    