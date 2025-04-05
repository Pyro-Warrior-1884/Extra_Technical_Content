#Not Perfect Algorithm : Moore Algorithm
# Question find the element that occurs more than n/2 times in array
arr = [1,3,1,3,2,3,2,3,2,3]
n = len(arr)

candidate = 0
count = 0 

for num in arr:
    if count == 0:
        candidate = num
        count = 1
    elif candidate == num:
        count += 1
    else:
        count -= 1
        
if arr.count(candidate) >= n/2:
    print(candidate)
else:
    print("None")
    
    