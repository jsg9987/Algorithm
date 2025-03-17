T = int(input())

for test_case in range(1, T + 1):
    nums = set()
    n = int(input())
    next_n = n
    result = 1

    while True:
        loop = 0
        li = list(str(next_n))
        for i in li:
            nums.add(int(i))

        next_n = (result + 1) * n
        for i in range(10):
            if i not in nums:
                loop = 1
                break

        if loop:
            result += 1
        else:
            break

    print(f"#{test_case} {n * result}")
