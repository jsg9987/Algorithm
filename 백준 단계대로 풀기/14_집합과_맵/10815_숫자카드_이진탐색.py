import sys

if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    m = int(input())
    arr2 = list(map(int, input().split()))

    for card in arr2:
        low, high = 0, n-1
        exist = False
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > card:
                high = mid - 1
            elif arr[mid] < card:
                low = mid + 1
            else:
                exist = True
                break
        print(1 if exist else 0, end= " ")