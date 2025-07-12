import re
for _ in range(int(input())):
    s = input()
    obj = r'[+-]?([0-9]+\.[0-9]+|\.[0-9]+)'
    print(bool(re.fullmatch(obj, s)))