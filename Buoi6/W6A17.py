n = int(input())
A = []
s = set()
for i in range (n):
  row = list(map(int, input().split()))
  A.append(row)
for i in range (n):
  ans = []
  a = 0
  b = i
  while b > -1:
    ans.append(A[a][b])
    a += 1
    b -= 1
  s.add(tuple(ans))
  ans = []
  a = n-i-1
  b = n-1
  while a < n:
    ans.append(A[a][b])
    a += 1
    b -= 1
  s.add(tuple(ans))
for i in range (n):
  A[i] = A[i][::-1]
for i in range (n):
  ans = []
  a = 0
  b = i
  while b > -1:
    ans.append(A[a][b])
    a += 1
    b -= 1
  s.add(tuple(ans))
  ans = []
  a = n-i-1
  b = n-1
  while a < n:
    ans.append(A[a][b])
    a += 1
    b -= 1
  s.add(tuple(ans))
for i in s:
  for j in i:
    print(j,end=" ")
  print()