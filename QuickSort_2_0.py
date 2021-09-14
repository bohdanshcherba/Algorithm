import time

comparisons = 0
swaps = 0


def partition_asc(arr, l, r):
    global comparisons
    global swaps
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        comparisons += 1
        if arr[j] <= pivot:
            i = i + 1
            swaps += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    swaps += 1

    return i + 1


def partition_desc(arr, l, r):
    global comparisons
    global swaps
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        comparisons += 1
        if arr[j] >= pivot:
            i = i + 1
            swaps += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    swaps += 1

    return i + 1


def quick_sort(arr, l, r, type):
    global comparisons

    comparisons += 1
    if l < r:
        if type == 'asc':
            q = partition_asc(arr, l, r)
        elif type == 'desc':
            q = partition_desc(arr, l, r)
        quick_sort(arr, l, q - 1, type)
        quick_sort(arr, q + 1, r, type)

    return arr

arr_for_sort = [3, 2, 90, 12, 21, -99, 13000, 213441, 212300, 9429402]


start = time.perf_counter()
arr = quick_sort(arr_for_sort, 0, len(arr_for_sort) - 1, 'asc')
end = time.perf_counter()

print('Quick Sort:')
print(f"Runtime of the program is {end - start:0.8f}")
print("comparisons: ", comparisons)
print("swap: ", swaps)
print(arr)
