A = eval(input())
B = {}
ans = 0
pos = 0
for i in A:
    if i not in B:
        B[i] = 1
    else: B[i] += 1
    if ans < B[i]:
        ans = B[i]
        pos = i
print(pos)