# used linear search
def find_fixedpoint(array):
    for i in range(len(array)):
        if i == array[i]:
            return f"{i} is == {array[i]}"
    return None


# used binary search
def binary_search(array, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    if array[mid] == mid:
        return f"{array[mid]} == {mid}"
    elif array[mid] > mid:
        return binary_search(array, low, mid - 1)
    else:
        return binary_search(array, mid + 1, high)
    return None


list_with_fixed_point = [-10, -5, 0, 3, 7, 9, 12, 13, 14]
result = find_fixedpoint(list_with_fixed_point)
result2 = binary_search(list_with_fixed_point, 0, len(list_with_fixed_point) - 1)
print(result)
print(result2)