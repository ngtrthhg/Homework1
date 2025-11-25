def find_n(a):
    s=0
    n=0
    while s<=a:
        n+=1
        s+=1/n
    return n
A=int(input())
print(find_n(A))