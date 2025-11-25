maxnum=-1000000000
minnum=1000000000
while 1:
    x=int(input())
    maxnum=max(maxnum,x)
    minnum=min(minnum,x)
    if x==-1:
        print(maxnum,minnum)
        break
