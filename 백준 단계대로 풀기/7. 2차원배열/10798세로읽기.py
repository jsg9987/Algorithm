# 공백 없는 경우에 글자 나누기
# readline으로 읽으면 1000\n인데 rstrip()하고 list함수 적용시 리스트가 만들어짐. 그리고 map 적용

# 입력 및 변수 초기화
# 1. 총 5줄 입력이 주어짐. 최대 15글자

import sys

inputF = sys.stdin.readline
col_max = 0
# 문제를 잘 읽자;;... 문자도 있다.
# 문제점 1. list로 변환하면 행마다 원소 개수가 다름.
arr = [list(inputF().rstrip()) for _ in range(5)]

# 행은 5까지밖에 없는데 j는 15까지다. 문제가됨.
# 배열의 열 길이 중 최대를 찾아서 i range로 넣자.
for i in range(5): 
    if len(arr[i]) > col_max:
        col_max = len(arr[i])

for i in range(col_max):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end="")
# 출력
# 1. 세로로 읽은 순서대로 글자들을 공백 없이 출력