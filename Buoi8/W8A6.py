class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.h + self.w)
    def scale(self, k):
        self.w *= k
        self.h *= k

w, h, k = map(int,input().split())
X = Rectangle(w, h)
X.scale(k)
print("{0:.2f}".format(X.area()),"{0:.2f}".format(X.perimeter()))