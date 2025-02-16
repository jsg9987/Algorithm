if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0

    for i in range(0, len(arr) -2):
        for j in range(i+1, len(arr) - 1):
            for k in range(j+1, len(arr)):
                if m >= arr[i] + arr[j] + arr[k] > result:
                    result = arr[i] + arr[j] + arr[k]

    print(result)
