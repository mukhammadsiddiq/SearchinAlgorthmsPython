# Linear search algorithm
def linear_search(arr, target):
    # Loop through each element in the array
    for i in range(0, len(arr)):
        # Check if the current element is equal to the target
        if arr[i] == target:
            return f"found {arr[i]}"
    # If the target is not found, return "not found"
    return "not found"

# Iterative binary search algorithm
def binary_search(arr, target):
    # Initialize the lower and higher indices
    lower_ind = 0
    higher_ind = len(arr) - 1

    # Loop while the lower index is less than or equal to the higher index
    while lower_ind <= higher_ind:
        # Calculate the middle index
        mid = (lower_ind + higher_ind) // 2
        # Check if the middle element is equal to the target
        if arr[mid] == target:
            return f"found {arr[mid]}"
        # If the target is less than the middle element, search in the left half
        elif target < arr[mid]:
            higher_ind = mid - 1
        # If the target is greater than the middle element, search in the right half
        else:
            lower_ind = mid + 1
    # If the target is not found, return "not found"
    return "not found"

# Recursive binary search algorithm
def binary_search_rec(array, target, low, high):
    # Base case: if the lower index is greater than the higher index
    if low > high:
        return "not found"
    else:
        # Calculate the middle index
        mid = (low + high) // 2
        # Check if the middle element is equal to the target
        if array[mid] == target:
            return f"found {array[mid]}"
        # If the target is greater than the middle element, search in the right half
        elif target > array[mid]:
            return binary_search_rec(array, target, mid + 1, high)
        # If the target is less than the middle element, search in the left half
        else:
            return binary_search_rec(array, target, low, mid - 1)

# Test array and target value
array = [1, 3, 5, 6, 9, 12, 13, 15, 16, 17, 18, 23, 24, 35]
target = 177

# Perform and print results of linear search
print("----------> linear search result <----------")
print(linear_search(array, target))

# Perform and print results of iterative binary search
print("----------> binary search result <----------")
print(binary_search(array, target))

# Perform and print results of recursive binary search
print("----------> recursive binary search result <----------")
print(binary_search_rec(array, target, 0, len(array) - 1))  # Corrected the high index to len(array) - 1
