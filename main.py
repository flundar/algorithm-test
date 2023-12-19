def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [22, 27, 16, 2, 18, 6]
insertion_sort(arr)
print("Sıralanmış dizi:", arr)


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [7, 3, 5, 8, 2, 9, 4, 15, 6]
selection_sort(arr)
print("Sıralanmış dizi:", arr)

