# linera search algorithm
def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return f"found {arr[i]}"
    return "not found"


# iterative binary search
def binary_search(arr, target):
    lower_ind = 0
    higher_ind = len(arr) - 1

    while lower_ind <= higher_ind:
        mid = (lower_ind + higher_ind) // 2
        if arr[mid] == target:
            return f"found {arr[mid]}"
        elif target < arr[mid]:
            higher_ind = mid - 1
        else:
            lower_ind = mid + 1
    return "not found"


# recursive binary search
def binary_search_rec(array, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if array[mid] == target:
            return f"found {array[mid]}"
        elif target > array[mid]:
            return binary_search_rec(array, target, mid + 1, len(array) - 1)
        else:
            return binary_search_rec(array, target, low, mid - 1)


array = [1, 3, 5, 6, 9, 12, 13, 15, 16, 17, 18, 23, 24, 35]
target = 177
print("----------> linear search result <----------")
print(linear_search(array, target))
print("----------> binary search result <----------")
print(binary_search(array, target))
print("----------> recursive binary search result <----------")
print(binary_search_rec(array, target, 0, len(array)))