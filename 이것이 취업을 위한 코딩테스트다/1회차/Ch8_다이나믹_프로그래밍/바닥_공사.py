n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    # 중간값들이 너무 커져서 정수 범위 오버플로우 방지
    # 나머지 연산은 덧셈과 곱셈 연산에서 결합법칙이 성립한다.
    d[i] = (d[i-1] + d[i-2] * 2) % 796796
    # d[i] = d[i-1] + d[i-2] * 2

print(d[n])

# 모듈러 분배 법칙 - 나머지 연산 분배 법칙
# 덧셈에 대한 나머지 연산
# (A+B) mod C = ((A mod C) + (B mod C)) mod C
# 곱셈에 대한 나머지 연산
# (A x B) mod C = ((A mod C) x (B mod C)) mod C