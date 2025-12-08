def is_prime(a):
    if a==2 or a==3: return True
    x=int(a**0.5)
    for i in range (3,x+1,2):
        if a%i==0 and a!=i: return False
    return True
a=int(input())
if is_prime(a): print("True")
else: print("False")
