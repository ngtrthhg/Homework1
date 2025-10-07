a,b,c=map(float,input().split())
x=0
if a+b>c: x+=1
if b+c>a: x+=1
if c+a>b: x+=1
if x<3: print ("Khong phai 3 canh cua tam giac")
else :
    x=(a+b+c)/2
    print ("{0:.1f}".format((x*(x-a)*(x-b)*(x-c))**0.5))