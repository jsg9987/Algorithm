for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0

    for i in range(2, len(arr) - 2):
        around_max = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        if arr[i] - around_max >= 1:
            result += arr[i] -around_max

    print(f"#{tc} {result}")
