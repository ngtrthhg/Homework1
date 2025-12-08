def swapp(a,b):
    a,b=b,a
    return [a,b]
x,y=map(int,input().split())
A=swapp(x,y)
print(A[0],A[1])
    