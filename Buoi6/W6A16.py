n,m = map(int,input().split())
A = []
for i in range (n):
  row = list(map(int, input().split()))
  A.append(row)
for i in A:
  for j in i:
    print(f"{j:>4}", end="")
  print()