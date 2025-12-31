n = int(input())
A = []
pos = 0

for i in range (n):
    x = input()
    A.append(x)
    if x == "Nemo": pos = i
    
print (A[pos-1],"and",A[pos+1])

    
