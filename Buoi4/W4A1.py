n=int(input())
s=0
#for i in range(n+1): s+=i
#print(s)
while n>0:
    s+=n
    n-=1
print(s)