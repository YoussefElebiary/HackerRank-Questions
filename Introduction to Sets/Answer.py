def average(array):
    # your code goes here
    st = set(array)
    return sum(st) / len(st)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)