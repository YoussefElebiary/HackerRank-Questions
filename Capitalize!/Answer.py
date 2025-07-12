import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    ans = ""
    for i in range(len(s)):
        if i == 0 and s[i].isalpha():
            ans += s[i].upper()
            continue
        if s[i - 1] == ' ' and s[i].isalpha():
            ans += s[i].upper()
            continue
        ans += s[i]
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()