def doiso(a):
    ans = 0
    count = 1
    for i in range ( len(a)-1 , -1 , -1 ):
        if ord(a[i]) >= 48 and ord(a[i]) <= 57:
            ans += ( ord(a[i]) - 48 ) * count
            count *= 10
    if a[0]=='-': ans *= -1
    return ans
def maytinh(a):
    x = ""
    fi = ""
    sc = ""
    for i in range(len(a)):
        if a[i] in '+-*/':
            x = a[i]
            fi = a[:i]
            sc = a[i+1:]
            break
    fi = doiso(fi)
    sc = doiso(sc)
    if x == '+': return fi + sc
    elif x == '-': return fi - sc
    elif x == '*': return fi * sc
    else: return fi / sc
    
S = input()
print("{0:.2f}".format(maytinh(S)))