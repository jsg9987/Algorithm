# 문제: N개의 수 주어짐. 오름차순 정렬 프로그램 작성

# 입력: 수의 개수 1 <= N <= 10⁶
#       N개의 줄에 수 주어짐 <= 10⁶, 단 수는 중복 X

# 출력: N개의 줄에 오름차순 정렬 결과 한줄에 하나씩 출력

import sys

inputF = sys.stdin.readline

arr = []
n = int(inputF().rstrip())

for i in range(n):
    arr.append(int(inputF().rstrip()))

def mergeSort(arr):
    
    if len(arr) <= 1:
        return arr
    # 파이썬 float 주의
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = mergeSort(left_arr)
    right_arr = mergeSort(right_arr)

    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    
    sorted = []
    i = j = 0
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted.append(left_arr[i])
            i += 1
        else:
            sorted.append(right_arr[j])
            j += 1
            
    sorted += left_arr[i:]
    sorted += right_arr[j:]
    
    return sorted

for i in mergeSort(arr):
    print(i)