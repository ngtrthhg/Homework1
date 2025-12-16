A = list(map(int,input().split()))
k = int(input())
ans = []
for i in range (len(A)):
  for j in range (i+1,len(A)):
    if A[i] + A[j] == k and (A[i],A[j]) not in ans:
      ans.append((A[i],A[j]))
print(ans)