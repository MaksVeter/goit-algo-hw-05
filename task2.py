def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            upper_bound = arr[mid]
            return (iterations, upper_bound)

    if low < len(arr):
        upper_bound = arr[low]

    return (iterations, upper_bound)


sorted_array = [1.1, 2.5, 3.7, 4.9, 5.3]
target_value = 3.0

result = binary_search(sorted_array, target_value)
print(result) 
