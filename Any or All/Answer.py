n = int(input())
ls = list(map(int, input().split(' ')))

def pal(n):
    x = str(n)
    return x == x[::-1]

if all(x > 0 for x in ls):
    if any(pal(x) for x in ls):
        print(True)
    else:
        print(False)
else:
    print(False)