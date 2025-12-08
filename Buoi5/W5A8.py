def Hamming_dist(a,b):
    ans=0
    while a!=0 or b!=0:
        if a%2 != b%2: ans+=1
        a//=2
        b//=2
    return ans

x,y=map(int,input().split())
print(Hamming_dist(x,y))