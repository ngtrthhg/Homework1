a=int(input())
a=str(a)
ans1=0
ans2=0
for i in a:
    if int(i)%2==0: ans1+=1
    else: ans2+=1
print("Chữ số chẵn: ",ans1)
print("Chữ số lẻ: ",ans2)