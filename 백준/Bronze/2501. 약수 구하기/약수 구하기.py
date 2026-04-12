import sys

inputF = sys.stdin.readline

n,k = map(int, inputF().rstrip().split())
arr = []

for i in range(1, n+1):
    if n % i == 0:
        arr.append(i)

# def mergeSort(arr, start, end):
#     mid = (start, end)/2
#     if start != end:
#         mergeSort(arr, start, mid)
#         mergeSort(arr, mid+1, end)
#     merge(arr, start, mid, end)

# def merge(arr, left, mid, right):
#     while(left<= mid & mid <= right):
#         if arr[left] > arr[mid]:
#             temp = arr[left]
#             arr[left] = arr[mid]
#             arr[mid] = temp
#             mid += 1
#         else:
#             left += 1

# mergeSort(arr, 0, len(arr))
if len(arr) < k:
    print(0)
else:
    print(arr[k-1])
