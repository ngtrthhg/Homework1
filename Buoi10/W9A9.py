def Median(a, b, c, d, e):
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if a > c:
        a, c = c, a
        b, d = d, b
    if b > e:
        b, e = e, b
    if b > c:
        b, c = c, b
    if c > e:
        c, e = e, c
    return c

a, b, c, d, e = map(int,input().split())
print(Median(a, b, c, d, e))