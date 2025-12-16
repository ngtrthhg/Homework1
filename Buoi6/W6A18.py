n,m,k = map(int,input().split())
A = []
ans = 0
for i in range (n):
    row = list(map(int, input().split()))
    A.append(row)
for i in range (n): ans += A[i][k-1]
print(ans)