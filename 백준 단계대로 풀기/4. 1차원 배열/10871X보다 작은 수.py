# 문제: 정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
#       이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하라.

# 입력: 첫째 줄에 N과 X 주어짐.
#       둘째 줄에 수열 A를 이루는 정수 N개가 주어짐.

# 출력: X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다.

# del 리스트명[인덱스]
# 리스트명.pop(인덱스)
# 리스트.remove(값)
import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
    
listA = list(map(int, sys.stdin.readline().rstrip().split()))
lenA = len(listA)
# len(listA)의 값이 계속해서 변해서 index out of range 에러 발생 -> 변하지 않는 값을 변수로 저장해둬야함.

# 1. 특정 값보다 같거나 큰 수를 리스트로 저장해둠.
# 2. 그 리스트에 있는 값으로 remove(값) 해서 값을 모두 없앰.
# 3. 모두 없앤 다음 출력

listB = []
for i in listA:
    if i>= x:
        listB.append(i)
    # print(listB)

i = 0
while i<len(listB):
    # print(f"함수 적용 전 i값: {i}")
    if listB[i] in listA:
        listA.remove(listB[i])
    # print(listA)
    # print(f"함수 적용 후 i값: {i}")
    # print(f"i값 줄어듬: {i}")
    i +=1
    # print(f"이번 분기에서 최종 i값: {i}")

for i in listA:
    print(i, end=" ")

