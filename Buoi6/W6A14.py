A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = []
for i in A:
  if i in B and i not in ans: ans.append(i)
print(ans)