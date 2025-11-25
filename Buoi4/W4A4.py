n=int(input())
if n<0: n*=-1
k=0
while n!=0:
    n//=10
    k+=1
print(k)