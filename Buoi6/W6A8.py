S = list(map(str,input().split()))
d = {}
for i in S: d[i] = 0
for i in S: d[i] += 1
print(d)