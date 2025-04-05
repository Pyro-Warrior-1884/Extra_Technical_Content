array_sum = []

n = int(input("Enter Size: "))
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())

sum = 0

for i in range(len(arr)):
    sum = 0
    for j in range(i,len(arr)):
        sum = sum + arr[j]
        if sum == 0:
            array_sum.append((i,j))
print(array_sum)

        