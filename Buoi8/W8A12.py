class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def mul(self, a):
        thuc = self.x * a.x - self.y * a.y
        ao = self.x * a.y + self.y * a.x
        self.x = thuc
        self.y = ao

a, b = map(float,input().split())
c, d = map(float,input().split())
X = ComplexNumber(a, b)
X.mul(ComplexNumber(c, d))
print(int(X.x), int (X.y))
