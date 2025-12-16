A = list(map(str,input().split()))
d = {}
for i in A: d[i] = []
for i in range (len(A)): d[A[i]]. append(i)
for i in d: d[i] = tuple(d[i])
print(d)