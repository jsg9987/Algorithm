T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    nums = set()
    result = 0

    while len(nums) < 10:
        result += 1
        nums.update(str(n * result))

    print(f"#{test_case} {n * result}")
