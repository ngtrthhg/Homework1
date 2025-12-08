def tongchuso(a):
    a=str(a)
    k=0
    for i in a: k+=int(i)
    return k
x=int(input())
print(tongchuso(x))