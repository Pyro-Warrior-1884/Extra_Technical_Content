def shell_sort(arr):
    n = len(arr)
    gap = n // 2  \

    while gap > 0:
        print("\ngap = ",gap)
        for i in range(gap, n):# 4-8
            temp = arr[i]
            print("\narr[i] = ",temp)
            j = i
            while j >= gap and arr[j - gap] > temp:
                print("j = ",j)                
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
            print("\n",arr)
            
        gap //= 2  

arr = [35, 33, 42, 10, 14, 19, 27, 44]
shell_sort(arr)
print("Sorted array:", arr)
