A = eval(input())
B = [1] * (len(A) + 5)
for i in range (len(A) - 1, -1, -1):
    for j in range (i - 1, -1, -1):
        if A[j] < A[i] and B[j] < B[i] + 1: B[j] = B[i] + 1
ans = 1
for i in range (len(A)): ans = max(ans, B[i])
print(ans)