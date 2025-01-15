# long int: 4byte 정수
# long long int: 8byte 정수 long 하나씩 늘때마다 4byte 늘어난다고 가정

# 입력: 첫 번째 줄에 문제의 정수 N(4<=n<= 1000, n은 4의 배수)

# 출력: Nbyte 정수까지 저장할 수 있다고 생각하는 정수 자료형 이름 출력

'''
python에서 _(언더스코어)에 대하여
1. 인터프리터에서 사용되는 경우: 마지막으로 실행된 결과값이 _라는 변수에 저장됨.
2. 값을 무시하고 싶은 경우: 
    x,_,y = (1,2,3) # x = 1, y = 3
    x, *_, y = (1,2,3,4,5) # x = 1, y = 5
    for _ in range(10): # 인덱스 무시
        do_something()
    # 특정 위치의 값 무시
3. 특별한 의미의 네이밍 하는 경우
4. 국제화/지역화 함수로 사용되는 경우
5. 숫자 리터럴값의 자릿수 구분을 위한 구분자로써 사용할 때
'''
n = int(input())
realN = int(n/4)
long = "long"
text = ""
for i in range(1, realN):
    long = long + " long"
print(long + " int")


# for _ in range(int(input())//4): # _를 사용하여 인덱스 무시, //를 사용하여 float 안되게 제어
#    print("long", end=" ") # print가 자동 줄바꿈(개행) 안하도록 , end로 공백을 구분자로 함.
    
# print("int")