arr = [1, 2, -3, 3, -1, 2]

storage = {}
pre_sum = 0
count = 0

storage[0] = 1

for i in range(len(arr)):
    pre_sum += arr[i]
    remove = pre_sum - 0

    if remove in storage:
        count += storage[remove]

    storage[pre_sum] = storage.get(pre_sum, 0) + 1

print(count)
