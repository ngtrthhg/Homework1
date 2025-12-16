A = list(map(int,input().split()))
k = int(input())
for i in range (len(A)):
  if i == k:
    print(i)