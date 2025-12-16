A = list(map(int,input().split()))
pos = 0
maxx = A[0]
for i in range (len(A)):
  if maxx < A[i]:
    maxx = A[i]
    pos = i
print(pos+1)