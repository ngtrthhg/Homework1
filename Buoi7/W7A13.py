A = list(map(int,input().split()))
n = len(A)
i = 0
j = 1
ans = 0

A.sort()
A.append(0)

while i <= n and j <= n:
    if abs(A[i] - A[j]) <= 1:
        ans = max(ans,j - i + 1)
        j += 1
    else : i = j
print(ans)

    