def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def binomial(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))


T = int(input())

for tc in range(T):
    n, m = map(int, input().split())

    print(binomial(m, n))
