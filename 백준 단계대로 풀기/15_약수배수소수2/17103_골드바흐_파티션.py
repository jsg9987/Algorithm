import sys

if __name__ == '__main__':
    inputF = sys.stdin.readline
    num = 1000000
    prime = []
    prime_list = [1] * num
    prime_list[0], prime_list[1] = 0, 0

    for i in range(2, int(num ** 0.5) + 1):
        if prime_list[i]:
            for j in range(i * i, num, i):
                prime_list[j] = 0

    # 🔥 모든 소수를 prime 리스트에 추가
    for i in range(2, num):
        if prime_list[i]:
            prime.append(i)

    t = int(inputF().rstrip())
    for _ in range(t):
        cnt = 0
        n = int(inputF().rstrip())

        for i in prime:
            if i >= n:
                break
            if prime_list[n - i] and i <= n - i:
                cnt += 1
        print(cnt)
