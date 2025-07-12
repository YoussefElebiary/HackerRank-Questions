import numpy as np
n, m, p = tuple(map(int, input().split()))

a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split())))
    
for _ in range(m):
    b.append(list(map(int, input().split())))
    
a = np.array(a)
b = np.array(b)
print(np.concatenate((a, b), axis=0))