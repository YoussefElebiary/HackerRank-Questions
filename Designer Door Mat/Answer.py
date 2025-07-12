n, m = tuple(map(int, input().split()))

for i in range(0, n // 2):
    print(('.|.'*(2 * i + 1)).center(m, '-'))

print("WELCOME".center(m, '-'))

for i in range(n // 2, 0, -1):
    print(('.|.'*(2 * i - 1)).center(m, '-'))