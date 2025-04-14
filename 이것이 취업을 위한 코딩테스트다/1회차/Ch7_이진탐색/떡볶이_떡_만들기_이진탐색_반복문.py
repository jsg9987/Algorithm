n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

cut_height = 0
while start <= end:
    temp_m = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            temp_m += x - mid

    if temp_m < m:
        end = mid - 1
    else:
        cut_height = mid
        start = mid + 1

print(cut_height)