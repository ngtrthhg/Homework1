import bisect

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, v=1):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


A = eval(input())
n = len(A)

X = []
for i in A: X.append(i)
X.sort()
for i in range (n):
    A[i] = bisect.bisect_left(X,A[i]) + 1

fwt = Fenwick(n)
result = [0] * n

for i in range(n - 1, -1, -1):
    pos = A[i]
    result[i] = fwt.query(pos - 1)
    fwt.update(pos, 1)

print(result)
