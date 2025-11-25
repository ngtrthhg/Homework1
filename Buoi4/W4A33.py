a=int(input())
a='0'+str(a)
count=0
ans=""
for i in range (len(a)-1,0,-1):
    count+=1
    ans=a[i]+ans
    if count==3 and i!=1:
        ans='.'+ans
        count=0
print(ans)