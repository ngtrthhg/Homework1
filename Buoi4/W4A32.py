a=input()
check1=0
check2=0
check3=0
check4=0
k=0
for i in range (len(a)):
    k=ord(a[i])
    if 65<=k and 90>=k: check1+=1
    elif 97<=k and 122>=k: check2+=1
    elif 48<=k and 57>=k: check3+=1
    else: check4+=1
if len(a)>6 and check1>0 and check2>0 and check3>0 and check4>0: print("Strong")
else : print("Weak")