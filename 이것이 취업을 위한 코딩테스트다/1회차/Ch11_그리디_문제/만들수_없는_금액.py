import sys
from itertools import combinations

inputF = sys.stdin.readline
n = int(inputF().rstrip())
coins = list(map(int, inputF().split()))
coins.sort()
target = 1

for i in range(n):
    if coins[i] > target:
        print(target)
        break
    target += coins[i]


# 오류! combinations의 시간복잡도는 2^n이므로 n이 커지면 무조건 시간 초과가 뜬다.
# 오류 가능성! 1부터 모든 경우를 검사할 때 놓칠 수 있는 가능성이 있다.
# possible = set()
#
# for i in range(1, n + 1):
#     tuples = combinations(coins, i)
#     for j in tuples:
#         possible.add(sum(j))
#
# for i in range(1, 1000000 * 1000 + 1):
#     if i not in possible:
#         print(i)
#         break

# 제일 작은 것부터 2개씩 더하며 target을 갱신하고 target-1까지 모든 경우를 만들 수 있는지 검사한다.
# 다음 coin이 target을 넘는 숫자이면 불가능해진다.
