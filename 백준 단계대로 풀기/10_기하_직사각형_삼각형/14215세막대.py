if __name__ == '__main__':
    a, b, c = map(int, input().split())
    arr = [a,b,c]
    max_side = max(arr)
    arr.remove(max_side)

    while sum(arr) <= max_side:
        max_side -= 1

    print(sum(arr) + max_side)

    '''
    arr = sorted(map(int, input().split()))
    result = li[0] + li[1] + min(li[2], li[0] + li[1] -1)
    # 두 변을 더한 값보다 가장 긴 변이 작아야함. 따라서 입력한 li[2] 또는 초과한다면 li[0] + li[1] -1까지 길이를 줄여야함.
    '''
