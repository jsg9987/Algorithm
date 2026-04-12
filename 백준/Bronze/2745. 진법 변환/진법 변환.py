import sys

def transformNum():
    inputF = sys.stdin.readline
    n, b = inputF().rstrip().split()
    b = int(b)
    resultSum = 0
    strInput = list(n)


    for i in range(len(strInput)):
        if strInput[len(strInput) - i - 1].isdigit():
            resultSum += int(strInput[len(strInput) - i - 1]) * pow(b, i)
        else:
            resultSum += (ord(strInput[len(strInput) - i - 1]) - ord('A') + 10) * pow(b, i)

    return resultSum
if __name__ == '__main__':

    print(transformNum())