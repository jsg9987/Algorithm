import sys

inputF = sys.stdin.readline

n = int(inputF().rstrip()) # n값을 오른쪽 공백 떼고 int로 변환시켜 저장
arr = list(map(int, inputF().rstrip())) # 공백없이 연속된 숫자를 map함수를 이용하여 int로 바꿔 list에 차례대로 저장
print(sum(arr))
