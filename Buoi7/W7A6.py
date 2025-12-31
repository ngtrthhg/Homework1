A = eval(input())
B = []

for i in range (len(A)):
    if i % 2 == 0:
        for j in A[i]: B.append(j)
    else:
        for j in range (len(A[i]) - 1, -1, -1): B.append(A[i][j])
        
print(B)