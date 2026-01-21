n = int(input())

for i in range(n):
    a = input()
    b = input()

    j = 0
    ok = True

    for ch in a:
        if j < len(b) and ch.upper() == b[j]:
            j += 1
        elif 'A' <= ch <= 'Z':
            ok = False
            break

    if j != len(b):
        ok = False

    print("YES" if ok else "NO")
