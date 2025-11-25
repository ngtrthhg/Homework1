a=input()
check1=0
check2=0
check3=0
k=0
for i in range (len(a)):
    k=ord(a[i])
    if 65<=k and 90>=k: check1+=1
    elif 97<=k and 122>=k: check2+=1
    elif 48<=k and 57>=k: check3+=1
print("Kí tự hoa:",check1)
print("Kí tự thường:",check2)
print("Kí tự số:",check3)