# 4/30 16:17 ~

num = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
str_num = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}

T = int(input())

for tc in range(1, T+1):
    _, n = input().split()
    n = int(n)
    nums = []
    for i in input().split():
        nums.append(num[i])
    nums.sort()
    for i in range(len(nums)):
        nums[i] = str_num[nums[i]]
    print(f"#{tc}")
    print(*nums)