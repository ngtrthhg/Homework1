a,b=map(float,input().split())
if a==0:
    if b==0:
        print("Vô số nghiệm")
    else :
        print("Vô nghiệm")
else :
    print("{0:.2f}".format(-b/a))