class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def subtract(self):
        return self.x - self.y
    def product(self):
        return self.x * self.y
    def divide(self):
        return self.x / self.y
    def power(self):
        return self.x ** self.y
    def mod(self):
        return self.x % self.y
    def set_numbers(self, a, b):
        self.x = a
        self.y = b

X = Calculator(0, 0)
while True:
    A = list(map(str,input().split()))
    if A[0] == "yes" or A[0] == "YES" or A[0] == "Yes": break
    if len (A) == 2:
        X.set_numbers(int(A[0]), int(A[1]))
    elif A[0] == '+': print(X.add())
    elif A[0] == '-': print(X.subtract())
    elif A[0] == '*': print(X.product())
    elif A[0] == '/': print(X.divide())
    elif A[0] == '^': print(X.power())
    elif A[0] == '%': print(X.mod())
    print("Bạn có muốn thoát ?")

    
