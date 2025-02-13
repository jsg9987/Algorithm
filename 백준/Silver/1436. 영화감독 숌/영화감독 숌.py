if __name__ == '__main__':
    arr = []
    x = 0
    while len(arr) < 10000:
        x += 1
        if '666' in str(x):
            arr.append(x)

    n = int(input())
    print(arr[n-1])
