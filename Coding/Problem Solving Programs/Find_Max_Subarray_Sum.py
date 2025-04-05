def max_subarray_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    max_sum = arr[0]
    current_sum = 0
    min_prefix_sum = 0  
    
    for num in arr:
        #print("Number: ",num)
        current_sum += num
        #print("Current Sum: ",current_sum)
        max_sum = max(max_sum, current_sum - min_prefix_sum)
        #print("Max Sum: ",max_sum)
        min_prefix_sum = min(min_prefix_sum, current_sum)
        #print("Min Prefix Sum: ",min_prefix_sum)
        #print()
    
    return max_sum

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum subarray sum:", max_subarray_sum(arr))  # Output: 6 (corresponding to [4, -1, 2, 1])
