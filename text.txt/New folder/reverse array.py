def reverse_array(arr, start, end):
    if start >= end:
        return
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    reverse_array(arr, start + 1, end - 1)


array = [1, 2, 3, 4, 5]
print("Original Array:", array)
reverse_array(array, 0, len(array) - 1)
print("Reversed Array:", array)
