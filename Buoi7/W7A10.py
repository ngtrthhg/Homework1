import bisect

A = eval(input())
m = int(input())

prefix = 0
ans = 0
seen = [0]

for x in A:
    prefix = (prefix + x) % m
    ans = max(ans, prefix)

    idx = bisect.bisect_right(seen, prefix)
    if idx < len(seen):
        ans = max(ans, (prefix - seen[idx] + m) % m)
    bisect.insort(seen, prefix)

print(ans)
