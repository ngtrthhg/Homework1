import ast
import bisect

A = ast.literal_eval(input())
B = ast.literal_eval(input())
X = []

for i in range (len(A)):
    X.append((A[i][1] - A[i][0] + 1,A[i][0],A[i][1]))
    
X.sort()
B.sort()

Ans = [0] * len(B)

for i in range (len(X) - 1, -1, -1):
    x1 = bisect.bisect_left (B, X[i][1])
    x2 = bisect.bisect_right (B, X[i][2])
    for j in range (x1, x2): Ans[j] = X[i][0]
    
for i in range (len(B)):
    if Ans[i] == 0: Ans[i] = -1
    
print(Ans)

    
