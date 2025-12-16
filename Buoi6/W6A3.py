A = tuple(map(int,input().split()))
k = int(input())
k %= len(A)
rotated = A[k:] + A[:k]
print(rotated)