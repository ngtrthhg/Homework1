import re

t = int(input())

for _ in range(t):
    s = input().strip()
    try:
        re.compile(s)
        print(True)
    except re.error:
        print(False)
