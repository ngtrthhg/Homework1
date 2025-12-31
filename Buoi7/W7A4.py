A  = list(map(int,input().split()))
d = {}
count = 1
for i in A: d[i] = 0
for i in A:
    d[i] += 1
    count = max(count, d[i])
for i in A:
    if count == d[i]:
        print (i,"xuat hien nhieu nhat, som nhat," ,d[i],"lan")
        break

