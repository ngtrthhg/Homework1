def collatz_length(n):
    count=1
    while n!=1:
        if n%2==0: n//=2
        else: n=3*n+1
        count+=1
    return count
A=[]
max_length=0
n=int(input())
for i in range (1,n+1):
    A.append(collatz_length(i))
    max_length=max(max_length,collatz_length(i))
for i in range (n):
    if A[i]==max_length:
        print(i+1,max_length)
        break