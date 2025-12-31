A = input()
a = input()
n = len(a)
ans = 0

for i in range(len(A) - n + 1):
    if A[i:i+n] == a:
        ans += 1
        i += n

print(ans)
