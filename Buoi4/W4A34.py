a=input()
b=input()
c=""
for i in range (len(a)-len(b)+2):
    c=a[i:i+len(b)]
    if c==b:
        print(a[0:i]+a[i+len(b):len(a)])
        break