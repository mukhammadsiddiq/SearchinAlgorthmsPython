def findPeak(array):
    low = 0
    high = len(array) - 1
    if len(array) <= 3:
        return None
    while low <= high:
        mid = (low + high) // 2
        left_mid = array[mid - 1] if mid - 1 > 0 else float("-inf")
        right_mid = array[mid + 1] if mid + 1 < len(array) else float("inf")
        if left_mid < array[mid] and right_mid > array[mid]:
            low = mid + 1
        elif left_mid > array[mid] and right_mid < array[mid]:
            high = mid - 1
        elif left_mid < array[mid] and right_mid < array[mid]:
            return f"Bitonic Point is {array[mid]}"
    return None


a = [1, 2, 3, 4, 5, 4, 3, 2, 1]
a1 = [1, 6, 5, 4, 3, 2, 1]
a2 = [1, 4, 3]

result = findPeak(a)
result1 = findPeak(a1)
result2 = findPeak(a2)
print(result)
print(result1)
print(result2)






