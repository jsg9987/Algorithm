if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0

    # 모든 경우의 수
    for i in range(0, len(arr) -2):
        for j in range(i+1, len(arr) - 1):
            for k in range(j+1, len(arr)):
                if m >= arr[i] + arr[j] + arr[k] > result:
                    result = arr[i] + arr[j] + arr[k]

    print(result)

    '''
    from itertools import combinations
    n, m = map(int, input().split())
    arr = list(map(int, input().split())
    result = 0
    
    for cards in combinations(arr, 3):
        temp_sum = sum(cards)
        if result < temp_sum <= m:
            result = temp_sum
    print(result)
    '''
