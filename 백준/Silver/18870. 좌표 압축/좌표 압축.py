if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    set_arr = sorted(list(set(arr)))
    dic = {set_arr[i] : i for i in range(len(set_arr))}

    for i in arr:
        print(dic[i], end= " ")

