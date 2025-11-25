def palin(x):
    x=str(x)
    a=len(x)//2
    for i in range (a):
        if x[i]!=x[len(x)-1-i]: return False
    return True
a=int(input())
k=0
n=""
while True:
    if palin(a):
        print(k,a)
        break
    n=str(a)[::-1]
    a=a+int(n)
    k+=1

    