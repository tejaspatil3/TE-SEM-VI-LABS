def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the current index is the minimum
        min_index = i

        # Find the index of the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
data = [64, 25, 12, 22, 11]
selection_sort(data)
print("Sorted array:", data)


# Time - O(n^2)

# def selectionSort(arr):
#     for i in range(len(arr)):
#         min = float('-inf')
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i],arr[j] = arr[j], arr[i]
#     return arr
    
# print(selectionSort([89,56,45,34,65,76]))