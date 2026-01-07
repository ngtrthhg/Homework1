class Triangle:
    def __init__(self, a1, a2, a3):
        self.x = a1
        self.y = a2
        self.z = a3
    def area(self):
        X = (self.x + self.y + self.z) / 2
        print("{0:.2f}".format((X * (X - a) * (X - b) * (X - c)) ** 0.5))
    def check(self):
        if self.x <= 0 or self.y <= 0 or self.z <= 0: return print("invalid")
        elif self.x >= self.y + self.z : return print("invalid")
        elif self.y >= self.x + self.z: return print("invalid")
        elif self.z >= self.x + self.y: return print("invalid")
        return self.area()

a, b, c = map(int,input().split())
X = Triangle(a, b, c)
X.check()
        