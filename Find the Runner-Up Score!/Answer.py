if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx = arr[0]
    prev_mx = arr[0]
    for i in range(n):
        if arr[i] > mx:
            prev_mx = mx
            mx = arr[i]
    print(prev_mx)