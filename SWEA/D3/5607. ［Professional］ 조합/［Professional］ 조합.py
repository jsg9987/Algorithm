# 4/29 21:41 ~
# 나눗셈에서는 mod 연산이 일반적으로 안된다.
# 따라서 나눗셈 대신 곱셈의 역원을 사용해야함.
MOD = 1234567891
MAX = 1000000

# 팩토리얼 미리 계산
fact = [1] * (MAX + 1)
for i in range(1, MAX+1):
    fact[i] = fact[i-1] * i % MOD

# 모듈러 역원 구하기 (페르마의 소정리)
def modinv(x):
    return pow(x, MOD - 2, MOD)

T = int(input())
for tc in range(1, T+1):
    n, r = map(int, input().split())
    
    result = fact[n] * modinv(fact[r]) % MOD
    result = result * modinv(fact[n-r]) % MOD
    
    print(f"#{tc} {result}")
