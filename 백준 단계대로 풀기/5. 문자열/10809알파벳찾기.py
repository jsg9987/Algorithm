import sys

inputF = sys.stdin.readline

strArr = list(inputF().rstrip())
resultArr = [-1 for i in range(26)]
# range(len(list)) 배열의 길이만큼 범위 지정해서 idx 구할 수도 있음. 아니면 i =0으로 설정해두고 키워갈 수도 있음.

# 똑같은 문자일 경우 첫번째 위치를 반환해주는 처리 필요!
for idx, value in enumerate(strArr):
    if resultArr[ord(value)-ord('a')]<0: # 이미 위치 찾은 경우는 if 빠져나가게
        resultArr[ord(value)-ord('a')] = idx

# 리스트를 바로 출력하지 않게 조심하자.
for i in resultArr:
    print(i)