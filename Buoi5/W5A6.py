def giaithua(a):
    ans=1
    for i in range(2,a+1):
        ans*=i
    return ans
x=int(input())
print(giaithua(x))