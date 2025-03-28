import sys
from collections import Counter

inputF = sys.stdin.readline
n = int(inputF())
nums = []

for i in range(n):
    nums.append(int(inputF().rstrip()))

nums.sort()
num_range = max(nums) - min(nums)

print(int(round(sum(nums) / n)))
print(nums[n//2])
cnt = Counter(nums).most_common(2) # 가장 많이 나온 순으로 n개를 반환
if len(nums) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(num_range)

