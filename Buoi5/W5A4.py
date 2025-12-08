def perfectnum(a):
    ans=0
    for i in range (1,a):
        if a%i==0: ans+=i
    if ans==a: return True
    else: return False
n=int(input())
if perfectnum(n): print("True")
else : print("False")