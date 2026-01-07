import math 
class cylinder:
    def __init__ (self, h1, r1):
        self.h = h1
        self.r = r1
    def dientich(self):
        return 2 * math.pi * self.r * (self.r + self.h)
    def thetich(self):
        return math.pi * self.r * self.r * self.h

a,b = map(int,input().split())
X = cylinder(a ,b)
print("{0:.2f}".format(X.dientich()))
print("{0:.2f}".format(X.thetich()))