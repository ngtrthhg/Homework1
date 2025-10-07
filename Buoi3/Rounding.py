a=float(input())
b=0
if a<0:
    if int(a)-a>a-int(a)+1: b=int(a)-1
    else: b=int(a)
    print(int(a),int(a)-1,b)
else :
    if int(a)+1-a>a-int(a): b=int(a)
    else: b=int(a)+1
    print(int(a)+1,int(a),b)