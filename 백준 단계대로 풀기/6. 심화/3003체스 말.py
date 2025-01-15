import sys

inputF = sys.stdin.readline

arrReal = [1,1,2,2,2,8]
# split()함수의 결과값이 리스트로 반환된다!
arrNow = list(map(int,inputF().rstrip().split()))

for i in range(len(arrReal)):
    arrReal[i] = arrReal[i]- arrNow[i]

for i in arrReal:
    print(i, end=" ")