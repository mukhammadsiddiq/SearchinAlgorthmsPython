def findPeak(array):
    # Initialize the low and high pointers for binary search
    low = 0
    high = len(array) - 1

    # If the array length is less than or equal to 3, return None as it can't have a bitonic peak
    if len(array) <= 3:
        return None

    # Start binary search loop
    while low <= high:
        # Calculate the mid index
        mid = (low + high) // 2

        # Set left_mid to the element to the left of mid, or negative infinity if mid is at the boundary
        left_mid = array[mid - 1] if mid - 1 >= 0 else float("-inf")

        # Set right_mid to the element to the right of mid, or positive infinity if mid is at the boundary
        right_mid = array[mid + 1] if mid + 1 < len(array) else float("inf")

        # Check if the current mid element is greater than both its neighbors
        if left_mid < array[mid] and array[mid] > right_mid:
            return f"Bitonic Point is {array[mid]}"

        # If the left neighbor is less than the mid element, move the search to the right half
        elif left_mid < array[mid]:
            low = mid + 1

        # If the left neighbor is greater than or equal to the mid element, move the search to the left half
        else:
            high = mid - 1

    # If no bitonic point is found, return None
    return None


# Test cases
a = [1, 2, 3, 4, 5, 4, 3, 2, 1]
a1 = [1, 6, 5, 4, 3, 2, 1]
a2 = [1, 4, 3]

# Call the findPeak function with each test case and print the results
result = findPeak(a)
result1 = findPeak(a1)
result2 = findPeak(a2)
print(result)  # Should print the bitonic point for array 'a'
print(result1)  # Should print the bitonic point for array 'a1'
print(result2)  # Should print None for array 'a2' because its length is <= 3
