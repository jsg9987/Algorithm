if __name__ == '__main__':
    a, b, c = map(int, input().split())
    arr = [a,b,c]
    max_side = max(arr)
    arr.remove(max_side)

    while sum(arr) <= max_side:
        max_side -= 1

    print(sum(arr) + max_side)
