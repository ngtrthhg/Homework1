A = eval(input())
B = []
for i in A:
    for j in i: B.append(j)
B.sort()
B.append([0, 0])
cnt = B[0][1]
C = []
for i in range (1, len(B)):
    if B[i - 1][0] == B[i][0]:
        cnt += B[i][1]
    else:
        C.append([B[i - 1][0], cnt])
        cnt = B[i][1]
print(C)

    