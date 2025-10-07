a=int(input())
s=0
if a<=50: s=a*1500
elif 50<a and a<=100: s=50*1500+(a-50)*2000
else: s=50*1500+50*2000+(a-100)*3000
print(s)