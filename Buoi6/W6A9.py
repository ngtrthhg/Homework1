d1 = eval(input())
d2 = eval(input())
d = {}
for i in d1: d[i] = 0
for i in d2: d[i] = 0
for i in d1: d[i] += d1[i]
for i in d2: d[i] += d2[i]
print(d)