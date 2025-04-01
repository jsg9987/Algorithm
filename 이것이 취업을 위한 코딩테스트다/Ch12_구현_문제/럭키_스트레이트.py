import sys

inputF = sys.stdin.readline
nums = list(map(int, list(inputF().rstrip())))

if sum(nums[:len(nums) // 2]) == sum(nums[len(nums) // 2:]):
    print("LUCKY")
else:
    print("READY")
