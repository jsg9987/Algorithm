# 5/4 21:45 ~
# 곱한 숫자가 단조 증가하는 수여야 하고, 그 중 최댓값을 출력하라.

T = int(input())

def possible(str_num):
    max_value = str_num[0]
    for i in range(1,len(str_num)):
        if str_num[i] < max_value:
            return False
        max_value = str_num[i]

    return True

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    result = -1

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            ij_mul = nums[i] * nums[j]
            if not possible(str(ij_mul)):
                continue
            result = max(result, ij_mul)

    print(f"#{tc} {result}")