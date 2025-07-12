import re
for _ in range(int(input())):
    s = input()
    if bool(re.fullmatch(r'[789]{1}\d*', s)) and len(s) == 10:
        print("YES")
    else:
        print("NO")