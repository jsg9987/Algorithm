def merge_sort(a, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(a, start, mid)
        merge_sort(a, mid+1, end)
        merge(a, start, mid, end)


def merge(a, start, mid, end):
    global cnt, res
    i = start
    j = mid + 1
    temp = []

    while i <= mid and j <= end:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1

    while i <= mid:
        temp.append(a[i])
        i += 1

    while j <= end:
        temp.append(a[j])
        j += 1

    i = start   
    t = 0

    while i <= end:
        a[i] = temp[t]
        cnt += 1
        if cnt == k:
            res = a[i]
            break
        i += 1
        t += 1

n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
res = -1
merge_sort(a,0,n-1)
print(res)