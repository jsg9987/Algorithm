# 이진 탐색(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


# 이진 탐색(반복문)
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우
        if array[mid] == target:
            return mid
        # 더 큰 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 더 작은 경우 오른쪽 확인
        else:
            start = mid + 1
    return None