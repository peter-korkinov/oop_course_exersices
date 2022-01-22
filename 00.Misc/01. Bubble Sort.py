def bubble_sort(arr, descending=False):
    sorted_arr_descending = []

    while arr:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        sorted_arr_descending.append(arr[-1])
        del arr[-1]

    if not descending:
        return [sorted_arr_descending[i] for i in range(len(sorted_arr_descending) - 1, -1, -1)]

    return sorted_arr_descending


def bubble_sort2(arr, descending=False):
    length = len(arr)

    for i in range(length - 1):
        modified = False

        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                modified = True

        if not modified:
            break

    if descending:
        return [arr[i] for i in range(len(arr) - 1, -1, -1)]

    return arr
