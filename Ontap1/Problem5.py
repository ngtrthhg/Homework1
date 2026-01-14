A = eval(input())
B = {}
ans = 1
for i in A:
    if i not in B:
        B[i] = 1
    else: B[i] += 1
    if ans < B[i]:
        ans = B[i]
        break
    
if ans < 2: print("False")
else : print("True")