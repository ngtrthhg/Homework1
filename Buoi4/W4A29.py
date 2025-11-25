def tongg(a,b):
    while len(a)<len(b): a='0'+a
    while len(b)<len(a): b='0'+b
    c=""
    nho=0
    tong=0
    for i in range (len(a)-1,-1,-1):
        tong=nho+ord(a[i])-48+ord(b[i])-48
        c=str(tong%10)+c
        nho=tong//10
    if nho>0: c='1'+c
    return c
a=input()
check=""
summ=""
for i in range(len(a)):
    if ord(a[i])>=48 and ord(a[i])<=57:check+=a[i]
    else:
        summ=tongg(summ,check)
        check=""
print(tongg(summ,check))
        