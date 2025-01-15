n = int(input())

'''
1. int를 문자열로 바꾸고 연결
2. f-string으로 문자열 구성
3. ,를 사용하여(한 칸씩 띄어지는 속성 가짐) 문자열 구성
'''

# range(1,10) -> 마지막 숫자는 제외, 3번째 인자는 얼만큼 간격 띌 것인지

for i in range(1,10):
    # print(str(n) + " * " + str(i) + " = "+ str(n*i))
    
    # print(n,"*",i,"=",n*i)
    # Python 프로그래밍 언어에서는 문자열과 정수를 직접 연결할 수 없습니다.
    print(f"{n}*{i} = {n*i}")


