A = input()
B = input()
C = input()
D = input()
X = [ (A, '1') , (B, '2'), (C, '3'), (D, '4')]
X.sort()
count = 65
ans = [''] * 4
for i in X:
    k = int(i[1])
    ans [k - 1] = chr(count)
    count += 1
for i in range (4): print(ans[i],end = " ")