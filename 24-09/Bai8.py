def layten(X) :
    a=0
    Ten=""
    for i in range (len(X)):
        if X[i]==':':
            a=i+2
            break
    for i in range (a,len(X)): Ten+=X[i]
    return Ten

A=input()
Trc=input()
Sau=input()
print("Ho va ten:",layten(A))
x=int(layten(Sau))-int(layten(Trc))
S=0
if x<=50: S=x*1984*1.08
else :
    if 51<=x and 100>=x: S=(50*1984+(x-50)*2050)*1.08
    else :
        if 101<=x and 200>=x: S=(50*1984+50*2050+(x-100)*2380)*1.08
        else :
            if 201<=x and 300>=x: S=(50*1984+50*2050+100*2380+(x-200)*2998)*1.08
            else :
                if 301<=x and 400>=x: S=(50*1984+50*2050+100*2380+100*2998+(x-300)*3350)*1.08
                else : S=(50*1984+50*2050+100*2380+100*2998+100*3350+(x-400)*3460)*1.08
print("Tien phai tra la:",int(round(S,0)))