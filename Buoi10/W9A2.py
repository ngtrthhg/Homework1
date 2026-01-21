matrix = []
k = 0
while True:
    s = input().strip()
    if s.isdigit():        
        k = int(s)
        break
    matrix.append(list(map(int, s.split())))

x = []
for i in matrix:
    for j in i:
        x.append(j)

x.sort()
print(x[k-1])