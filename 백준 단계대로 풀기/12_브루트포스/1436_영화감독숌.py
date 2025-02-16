import time

if __name__ == '__main__':
    start_time = time.time()
    arr = []
    x = 0
    while len(arr) < 10000:
        x += 1
        if '666' in str(x):
            arr.append(x)

    n = int(input())
    print(arr[n-1])
    end_time = time.time()
    print(end_time - start_time)
