A = set(map(str,input().split()))
B = set(map(str,input().split()))
C = A - B
D = B - A
E = B & A
print(list(C),list(D),list(E))