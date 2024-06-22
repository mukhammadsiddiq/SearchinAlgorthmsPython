# Function using linear search to find a fixed point in the array
def find_fixedpoint(array):
    # Iterate through the array
    for i in range(len(array)):
        # Check if the current index i is equal to the value at index i
        if i == array[i]:
            return f"{i} is == {array[i]}"  # Return the index and value if they are equal
    return None  # Return None if no fixed point is found


# Function using binary search to find a fixed point in the array
def binary_search(array, low, high):
    # Base case: if the low index exceeds the high index, no fixed point is found
    if low > high:
        return None

    # Calculate the mid index
    mid = (low + high) // 2

    # Check if the value at the mid index is equal to the mid index
    if array[mid] == mid:
        return f"{array[mid]} == {mid}"  # Return the index and value if they are equal

    # If the value at mid is greater than mid, search in the left half
    elif array[mid] > mid:
        return binary_search(array, low, mid - 1)

    # If the value at mid is less than mid, search in the right half
    else:
        return binary_search(array, mid + 1, high)

    return None  # This line is redundant as it is never reached


# Example list containing a fixed point
list_with_fixed_point = [-10, -5, 0, 3, 7, 9, 12, 13, 14]

# Using linear search to find a fixed point
result = find_fixedpoint(list_with_fixed_point)

# Using binary search to find a fixed point
result2 = binary_search(list_with_fixed_point, 0, len(list_with_fixed_point) - 1)

# Print the results of both searches
print(result)
print(result2)
