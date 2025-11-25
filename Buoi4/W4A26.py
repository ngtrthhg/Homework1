a=int(input())
nho1=1
nho2=1
nho3=2
ans=1
check=0
for i in range (1000000):
    if nho3>=nho2 and nho2>=nho1: nho1=nho2+nho3
    elif nho3>=nho2 and nho1>=nho3: nho2=nho3+nho1
    elif nho2>=nho3 and nho1>=nho3: nho3=nho2+nho1
    check=max(nho1,max(nho2,nho3))
    if check>a:
        print(ans)
        break
    else: ans=check  