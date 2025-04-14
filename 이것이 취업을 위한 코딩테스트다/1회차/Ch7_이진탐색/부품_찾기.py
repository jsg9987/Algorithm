import sys


def binary_search(arr, x, start, end):
    if start > end:
        return False
    mid = (start + end) // 2

    if arr[mid] == x:
        return True
    elif arr[mid] > x:
        return binary_search(arr, x, start, mid - 1) # 앞에 return을 안붙였을 때에는 재귀 호출 결과가 최종 결과로 return이 이루어지지 않았다.
    else:
        return binary_search(arr, x, mid + 1, end)


inputF = sys.stdin.readline

n = int(inputF())
products = sorted(list(map(int, inputF().rstrip().split())))
m = int(inputF())
wants = list(map(int, inputF().rstrip().split()))

for i in wants:
    if binary_search(products, i, 0, len(products) - 1):
        print("yes", end=' ')
    else:
        print("no", end=' ')


# 이진 탐색 소스코드 구현(반복문)
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None
