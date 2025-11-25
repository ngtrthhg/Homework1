def is_prime(a):
    if a==2 or a==3: return True
    x=int(a**0.5)
    for i in range (2,x+1):
        if a%i==0: return False
    return True
n=-1
while n<0 or n%1!=0: n=float(input())
if is_prime(n): print("True")
else : print("False")

    