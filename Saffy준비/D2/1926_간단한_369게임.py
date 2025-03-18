n = int(input())
nums = [i for i in range(1, n + 1)]

for num in nums:
    arr = list(map(int, list(str(num))))
    cnt = 0

    if 3 in arr or 6 in arr or 9 in arr:
        for i in arr:
            if i == 3 or i == 6 or i == 9:
                cnt += 1
        print("-" * cnt, end=" ")
    else:
        print(num, end=" ")

