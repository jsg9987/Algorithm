from math import factorial

n, k = map(int, input().split())

print(factorial(n) // (factorial(n - k) * factorial(k)))

'''
li = [i for i in range(n)]
print(len(list(combinations(li, k)))
'''

'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(n) // (factorial(k) * factorial(n -k))))
'''

'''
#이항 계수
def bino_coef(n, k): #4C3-> 3C2 + 3C3 (선택한 경우:나머지 3개 중 2개를 선택, 선택 안한 경우: 나머지 3개중 3개를 택)
    if k == 0 or n == k:
        return 1
    return bino_coef(n-1, k-1) + bino_coef(n-1, k)
'''
