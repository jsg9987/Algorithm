import sys 
inputF = sys.stdin.readline

n,m = map(int, inputF().rstrip().split())

arr = [[0 for i in range(n+1)]] # 원본 배열 첫째 줄 모두 0으로 채우기
dp = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(n):
		arr_row = [0] + list(map(int,inputF().rstrip().split())) # 왼쪽 한칸 0 채우고
		arr.append(arr_row) # 아래로 한 줄씩 채우기

for i in range(1,n+1):
		for j in range(1,n+1):
				dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j]
for  i in range(m):
		x1,y1,x2,y2 = map(int,inputF().rstrip().split())
		result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
		print(result)