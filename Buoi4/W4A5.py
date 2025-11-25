n=int(input())
k=0
A=list(map(int,input().split()))
for i in A:
    if i==42: k=1
if k==1: print("I've found the meaning of life!")
else : print("It's a joke!")