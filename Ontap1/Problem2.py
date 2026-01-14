A = input().split()
B = {}
Ans = []

for i in A:
    if i not in B:
        B[i] = 1
    else: B[i] += 1
    
for i in B: Ans.append((B[i], i))

Ans.sort()
Ans.reverse()

Ans = [Ans[0][1], Ans[1][1], Ans[2][1]]
Ans.sort()

print(Ans)
    
    