A = list(map(str,input().split()))
d = {}
d_new = {}
for i in range (0,len(A),2):
  d[A[i]] = A[i + 1]
for i in d: d_new[d[i]] = i
print(d_new)