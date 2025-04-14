# 4/14 21:15 ~
# 주어진 수들로 M번 더해서 가장 큰 수를 만들어야 한다.
# 조건: 배열의 특정한 인덱스에 해당하는 수가 연속 K번을 초과할 수 없다.
# 아이디어: 내림차순으로 정렬하고 현재 더하는 순서가 K로 나눠 떨어진다면 li[1]을 더한다.
# 2 <= N <= 1000, 1 <= M, K <= 10,000

# n, m, k = map(int, input().split())
# li = list(map(int, input().split()))
# li.sort(reverse=True)
# result = 0
#
# for i in range(1, m + 1):
#     if i % (k + 1) != 0:
#         result += li[0]
#     elif i % (k + 1) == 0:
#         result += li[1]
#
# print(result)


# for문을 사용하지 않고 묶음으로 풀 수도 있다.
def solution():
    n, m, k = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort(reverse=True)

    first = li[0]
    second = li[1]
    loop = m // (k + 1)  # 반복 횟수
    remain_cnt = m % (k + 1)
    result = (first * k + second) * loop + first * remain_cnt

    return print(result)


solution()
