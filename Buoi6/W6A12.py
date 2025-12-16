A = list(map(str,input().split()))
A.sort()
d = {}
count = 0
for i in A: d[i] = 0
for i in A: 
  d[i] += 1
  count = max(count,d[i])
for i in d:
  if d[i] == count:
    print(i)
    break