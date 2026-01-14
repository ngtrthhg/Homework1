A = eval(input())
Ans = []
for i in A:
    if i % 3 == 0 and i % 2 != 0: Ans.append(i*i)
print(Ans)