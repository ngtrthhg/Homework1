def position(A,a):
    for i in range (len(A)):
        if a==A[i]: return i+1
    return -1
X=list(map(int,input().split()))
x=int(input())
print(position(X,x))