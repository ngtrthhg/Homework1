m,n=map(int,input().split())
x=(m*4-n)/2
if x%1!=0: print("invalid")
else : print(int(x),int(m-x))