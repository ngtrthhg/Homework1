A  = list(map(int,input().split()))
a = int(input())
n = len(A)
ans = 0
for i in range (n):
    for j in range (i+1,n):
        if A[i] + A[j] == a:
            ans += 1
print(ans)
        