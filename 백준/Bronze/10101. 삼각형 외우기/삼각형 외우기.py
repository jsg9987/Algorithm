if __name__ == '__main__':
    arr = []
    arr.append(int(input()))
    arr.append(int(input()))
    arr.append(int(input()))

    if arr.count(60) == 3:
        print("Equilateral")
    elif sum(arr) == 180 and len(set(arr)) == 2:
        print("Isosceles")
    elif sum(arr) == 180 and len(set(arr)) == 3:
        print("Scalene")
    elif sum(arr) != 180:
        print("Error")
