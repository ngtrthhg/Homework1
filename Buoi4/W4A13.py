def tonguoc(n):
    ans=0
    for i in range (1,n):
        if n%i==0: ans+=i
    return ans
a,b=map(int,input().split())
if a==tonguoc(b) and b==tonguoc(a): print("true")
else: print("false")