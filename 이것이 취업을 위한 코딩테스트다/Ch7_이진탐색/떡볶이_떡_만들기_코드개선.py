def binary_search(arr, m, start, end):
    if start > end:
        return
    cut_height = (start + end) // 2
    temp_m = 0

    for x in arr:
        if x - cut_height <= 0:
            temp_m += 0
        else:
            temp_m += x - cut_height

    if temp_m == m:
        return cut_height
    elif temp_m > m:
        return binary_search(arr, m, cut_height + 1, end)
    else:
        return binary_search(arr, m, start, cut_height - 1)


n, m = map(int, input().split())
arr = list(map(int, input().split()))

cut_height = binary_search(arr, 6, 0, max(arr))
print(cut_height)