import sys
# import traceback

# 런타임 에러(ValueError): 문자가 들어가거나, 2개 이상 등 에러에 대한 대처가 안됨.
# while 1:
#     a,b = map(int, sys.stdin.readline().rstrip().split())
#     print(a+b)
while 1:
    try:
        a,b = map(int, sys.stdin.readline().rstrip().split())
        print(a+b)
    except:
        # print(traceback.format_exc())
        break