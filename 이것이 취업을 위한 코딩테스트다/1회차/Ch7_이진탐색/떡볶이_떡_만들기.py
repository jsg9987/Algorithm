def binary_search(arr, m, start, end): # 굳이 높이를 떡 길이와 일치하게 잡은게 패착이었던 것 같다. 그렇게 하지 않아도 이진 탐색을 하기 때문에 시간 초과하지 않았을 듯
    if start > end:
        return (start - 1 + end) // 2
    mid = (start + end) // 2
    cut_height = arr[mid]
    temp_m = 0
    for x in arr:
        if x - cut_height <= 0:
            temp_m += 0
        else:
            temp_m += x - cut_height

    if temp_m == m: #arr값에서 cut_height보다 작은 떡을 짜를 때 0이 나오게 해야함.
        return mid
    elif temp_m < m:
        return binary_search(arr, m, mid + 1, end)
    else:
        return binary_search(arr, m, start, mid - 1)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

idx = binary_search(arr, m, 0, len(arr) - 1)
temp_m = 0
for cut_height in range(arr[idx], arr[idx + 1] + 1): # 마지막 인덱스 list out of range
    for x in arr:
        if x - cut_height <= 0:
            temp_m += 0
        else:
            temp_m += x - cut_height
    if  temp_m == m:
        print(cut_height)