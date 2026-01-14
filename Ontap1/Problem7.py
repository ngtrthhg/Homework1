A = eval(input())
B = []
for i in A:
    for j in i:
        if j % 2 == 0: B.append(j)
print(B)