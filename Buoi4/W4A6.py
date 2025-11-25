def is_prime(a):
    if a==2 or a==3: return True
    x=int(a**0.5)
    for i in range (2,x+1):
        if a%i==0 and a!=i: return False
    return True
a,b=map(int,input().split())
s=0
for i in range (a,b+1):
    if is_prime(i): s+=i
print(s)
