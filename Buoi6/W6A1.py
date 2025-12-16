def check(x, Y):
  for i in Y:
    if x == i: return False
  return True
A = list(map(int,input().split()))
B = []
for i in A:
  if check(i,B) : B.append(i)
print(B)