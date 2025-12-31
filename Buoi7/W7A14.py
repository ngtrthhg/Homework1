n = int(input())
A = list(map(int,input().split()))
B = []
check = True

for i in range (n): B.append((A[i], i))

B.sort()
B.reverse()

for i in B:
    if i[0] == 7:
        print(i[1],end = " ")
        check = False
        
if check: print("Not Found")

