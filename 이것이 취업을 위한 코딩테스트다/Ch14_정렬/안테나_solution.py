# 안테나와 집 사이의 거리 절대값의 합이 최소가 되려면 중앙값을 선택해야한다.
# 평균은 제곱 거리의 합을 최소화 시킨다.

n = int(input())
li = list(map(int, input().split()))
li.sort()

print(li[(n - 1) // 2]) # 홀수로 만들면 항상 앞에 값을 선택 가능
