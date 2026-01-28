def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1


try:
    a = int(input())

    if a <= 0:
        print("NO")
    else:
        print("YES" if is_happy_number(a) else "NO")

except ValueError:
    print("NO")
