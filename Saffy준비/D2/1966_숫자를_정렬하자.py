T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    print(f"#{tc}", *nums)