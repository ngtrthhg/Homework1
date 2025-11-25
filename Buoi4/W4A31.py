a=input()
ans=0
for i in a:
    if ord(i)>=48 and ord(i)<=57: ans+=int(i)
print(ans)