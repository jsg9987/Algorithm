import sys

inputF = sys.stdin.readline
n,m = map(int, inputF().rstrip().split())
arr = list(map(int, inputF().split()))
weights = [0] * 11
result = 0

# for weight in arr:
#     weights[weight] += 1
#
# for i in range(len(weights)-1,0,-1):
#     result += weights[i] * sum(weights[i-1::-1])

# sum도 시간복잡도도 O(N)이기 때문에 위 코드 O(N^2)
for i in range(1, m+1):
    n -= weights[i] # 무게가 i인 볼링공의 개수(A가 선택한 공 개수) 제외 -> B가 선택하는 개수
    result += weights[i] * n

print(result)