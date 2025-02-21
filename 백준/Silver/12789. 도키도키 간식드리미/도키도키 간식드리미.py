if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    ST = []
    cnt = 1

    for num in nums:
        ST.append(num)
        while ST and ST[-1] == cnt:
            ST.pop(-1)
            cnt += 1
    
    if not ST:
        print("Nice")
    else:
        print("Sad")
