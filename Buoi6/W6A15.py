A = list(map(str,input().split()))
k = int(input())
d = {}
for i in range (0,len(A),2):
  if int(A[i+1]) > k:
    d[A[i]] = int(A[i+1])
print(d)