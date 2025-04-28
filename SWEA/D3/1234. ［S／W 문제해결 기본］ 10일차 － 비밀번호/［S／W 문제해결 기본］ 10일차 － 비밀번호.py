# 4/28 17:17 ~
# 같은 번호로 붙어있는 쌍 소거하고 남은 번호

for tc in range(1, 11):
    n, nums = input().split()
    n = int(n)
    nums = list(map(int, nums))
    idx = 0
    compare_num = nums[idx]

    while idx != len(nums) - 1:
        if compare_num == nums[idx+1]:
            del nums[idx:idx+2]
            idx -= 1
            compare_num = nums[idx]
        else:
            idx += 1
            compare_num = nums[idx]

    nums = list(map(str, nums))
    print(f"#{tc} {''.join(nums)}")