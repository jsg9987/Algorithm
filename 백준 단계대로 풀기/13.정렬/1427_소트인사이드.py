if __name__ == '__main__':
    n = int(input())
    arr = list(str(n))
    arr2 = list(map(int, arr))
    arr2.sort(reverse=True)

    # print(*arr2, sep="")
    for i in arr2:
        print(i, end="")