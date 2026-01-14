n = int(input())
if n % 2  == 0:
    cow = 0
    chic = 0
    ans = []
    if n == 0: ans.append((0, 0))
    n = n // 2
    for i in range (n + 1):
        if (n - i) % 2 == 0: ans.append((i, int((n - i) / 2)) )
    print(ans)