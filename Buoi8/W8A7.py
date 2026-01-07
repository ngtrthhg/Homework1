class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self , a, b):
        self.x = self.x*b + a*self.y
        self.y *= b
    def sub(self , a, b):
        self.x = self.x*b - a*self.y
        self.y *= b
    def mul(self , a, b):
        self.y *= b
        self.x *= a
    def div(self , a, b):
        self.y *= a
        self.x *= b
    def shorten(self):
        for i in range (max(self.x,self.y), 0, -1):
            if self.x  % i == 0 and self.y % i == 0:
                self.x /= i
                self.y /= i
                break
    def out(self):
        print (str(int(self.x)) + '/' + str(int(self.y)))

A = list(map(str,input().split()))
a = int(A[0])
b = int(A[1])
c = int(A[3])
d = int(A[4])
X = Fraction(a, b)

if A[2] == '+': X.add(c, d)
elif A[2] == '-': X.sub(c, d)
elif A[2] == '*': X.mul(c, d)
elif A[2] == '/': X.div(c, d)
X.shorten()

X.out()