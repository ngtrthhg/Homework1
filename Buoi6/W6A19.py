A = list(map(int,input().split()))
pos = 1
for i in range (len(A)):
  if A[i] > A[pos-1] : pos = i+1
print(pos)