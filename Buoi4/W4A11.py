n=int(input())
ans=0
for i in range (2,n+1,2):
    if n%i==0: ans+=1
print(ans)