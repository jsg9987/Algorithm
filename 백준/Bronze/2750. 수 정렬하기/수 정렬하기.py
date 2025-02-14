if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(int(input()))

    arr.sort()

    for num in arr:
        print(num)
