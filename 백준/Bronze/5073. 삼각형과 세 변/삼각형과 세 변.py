if __name__ == '__main__':
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == 0:
            break
        arr = [a,b,c]
        arr.remove(max(a,b,c))

        if max(a,b,c) >= sum(arr):
            print("Invalid")
        else:
            if a == b == c:
                print("Equilateral")
            elif a == b or b == c or c == a:
                print("Isosceles")
            elif a != b != c:
                print("Scalene")

