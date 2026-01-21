A = list(map(int, input().split()))
B = list(map(int, input().split()))
i = 0
j = 0
res = []
while i < len(A) and j < len(B):
    if A[i] > B[j]:
        res.append(B[j])
        j += 1
    else :
        res.append(A[i])
        i += 1
res.extend(A[i:])
res.extend(B[i:])
print(res)