def print_array(arr, index):
    if index >= len(arr):
        return
    print(arr[index])
    print_array(arr, index + 1)


array = [1, 2, 3, 4, 5]
print_array(array, 0)
