if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(int(input()))

    # arr.sort()
    for _ in range(n):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

    for num in arr:
        print(num)
