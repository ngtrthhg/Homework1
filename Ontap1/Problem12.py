def check (A):
    odd = 0
    even = 0
    for i in A:
        if i % 2 == 0: even += 1
        else: odd += 1
    n = len(A)
    if odd > 0 and even > 0: return True
    if odd == n and n % 2 == 0: return False
    if even == n : return False

A = eval(input())
print(check(A))
