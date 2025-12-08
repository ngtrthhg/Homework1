def ktra(a,b):
    S1=[]
    S2=[]
    for i in range (260):
        S1.append(0)
        S2.append(0)
    for i in range (len(a)):
        if S1[ord(a[i])] == 0 and S2[ord(b[i])] == 0:
            S1[ord(a[i])] = ord(b[i])
            S2[ord(b[i])] = ord(a[i])
        elif S1[ord(a[i])] != ord(b[i]) or S2[ord(b[i])] != ord(a[i]): return "false"
    return "true"


a,b=map(str,input().split())
print(ktra(a,b))