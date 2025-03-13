import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    li = map(int, input().split())
    num_sum = 0

    for i in li:
        if i % 2 != 0:
            num_sum += i

    print("#" + str(test_case) + " " + str(num_sum))
