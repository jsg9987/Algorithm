# 4/19 17:33~
# 금액을 오름차순으로 정렬 후 다음 가능한 금액을 화폐를 더한 것보다 1 크게 지정하고, 그것보다 다음 화폐가 더 크면 불가능하다.
n = int(input())
li = sorted(list(map(int, input().split())))
# next_check = 1
# next_coin = li[0]
# coin_sum = li[0]
# idx = 1
#
# while True:
#     if next_coin > next_check:
#         print(next_check)
#         break
#     next_check = coin_sum + 1
#     next_coin = li[idx]
#     coin_sum += next_coin
#     idx += 1 # index를 임의로 지정하고 있기 때문에 n이 1일 때 에러, 또한 불안정한 코드
target = 1

for coin in li:
    if coin > target:
        break
    target += coin

print(target)
