def binary_search(arr, target):
    if arr:
        low, high = 0, len(arr)-1
        while low <= high:
            mid = (low + high) // 2
            if target == arr[mid]:
                return mid
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
print(result)
