def find_closest(array, target):
    # Initialize minimum difference to infinity
    min_diff = float("inf")
    # Initialize low and high pointers for binary search
    low = 0
    high = len(array) - 1
    # Variable to store the closest number found
    closest_number = None

    # If the array is empty, return None
    if len(array) == 0:
        return None
    # If the array has only one element, return that element
    if len(array) == 1:
        return array[0]

    # Perform binary search to find the closest number
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # Calculate the difference between target and the element just right to mid, if it exists
        if mid + 1 < len(array):
            min_diff_right = abs(array[mid + 1] - target)
        # Calculate the difference between target and the element just left to mid, if it exists
        if mid > 0:
            min_diff_left = abs(array[mid - 1] - target)

        # Update the closest number if a smaller difference is found on the right side
        if mid + 1 < len(array) and min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_number = array[mid + 1]
        # Update the closest number if a smaller difference is found on the left side
        if mid > 0 and min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_number = array[mid - 1]

        # If the middle element is less than the target, search the right half
        if array[mid] < target:
            low = mid + 1
        # If the middle element is greater than the target, search the left half
        elif array[mid] > target:
            high = mid - 1
        # If the middle element is equal to the target, return it as the closest number
        else:
            return array[mid]

    # Return the closest number found
    return closest_number


# Example usage
array = [2, 4, 6, 7, 8, 9, 11, 13, 15]
target = 3
result = find_closest(array, target)
print(result)  # Output: 2
