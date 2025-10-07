a=float(input())
b=float(input())
c=float(input())
if a+b>c and b+c>a and a+c>b:
    if a==b and b==c: print("Tam giác đều")
    elif a==b or b==c or c==a: print("Tam giác cân")
    else : print("Tam giác thường")     
else : print("Không phải tam giác")