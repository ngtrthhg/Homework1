def ktra(a):
    s=""
    dem=0
    while a>0:
        digit=a%10
        a//=10
        dem=s.find(str(digit))
        if dem>-1: return False
        s+=str(digit)
    return True
n=int(input())
for i in range (1,int(n**0.5)+1):
    if ktra(i*i): print(i*i,end=" ")
    