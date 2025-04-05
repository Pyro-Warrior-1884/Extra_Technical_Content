Size = int(input("Enter Size: "))
strs =  [input() for _ in range(Size)]

pre = ""
var = strs[0]

for j in range(len(var)):
    count = 0
    for i in range(1, len(strs)):    
        if j < len(strs[i]) and strs[i][j] == var[j]:
            count += 1
    if count == len(strs) - 1:
        pre += var[j]
    else:
        break

print(pre)

        