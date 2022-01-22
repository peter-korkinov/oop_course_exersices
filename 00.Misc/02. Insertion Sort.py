def insertion_sort(arr):
    sorted_arr = [arr[0]]

    for i in range(1, len(arr)):
        sorted_len = len(sorted_arr)
        current = arr[i]

        for j in range(sorted_len - 1, -1, -1):
            if arr[i] > sorted_arr[j]:
                if j == sorted_len - 1:
                    sorted_arr.append(current)
                    break

                sorted_arr.insert(j + 1, current)
                break

            if j == 0:
                sorted_arr.insert(0, current)

    return sorted_arr


def insertion_sort2(arr):
    sorted_arr = []
    length_sorted = 0

    for i in arr:
        if not sorted_arr:
            sorted_arr.append(arr[0])
            continue

        for j in range(length_sorted - 1, -1, -1):
            if arr[i] > sorted_arr[j]:
                if j == length_sorted - 1:
                    sorted_arr.append(arr[i])
                    length_sorted += 1
                    break

                bigger_than_i = [sorted_arr[k] for k in range(j + 1, length_sorted)]
                sorted_arr = [sorted_arr[L] for L in range(j + 1)]
                sorted_arr.append(arr[i])
                sorted_arr.extend(bigger_than_i)
                length_sorted += 1
                break

            if j == 0:
                temp = [k for k in sorted_arr]
                sorted_arr = [arr[i]]
                sorted_arr.extend(temp)
                length_sorted += 1

    return sorted_arr


aroo = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, 12]
print(insertion_sort2(aroo))
print(sorted(aroo))
