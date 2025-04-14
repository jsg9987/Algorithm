import time
# Memoization

start_time = time.time()
d = [0] * 100

# Top down(recursion)
def fibo(x):
    # 종료 조건(1 or 2일 때)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있으면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 도출
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
end_time = time.time()
print(start_time - end_time)

# 반복문 사용(bottom -up)
# d = [0] * 100
#
# d[1] = 1
# d[2] = 1
# n = 99
#
# for i in range(3, n+1):
#     d[i] = d[i-1] + d[i-2]