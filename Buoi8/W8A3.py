class point_2D:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1
    def kiemtra(self):
        if self.x == 0 and self.y == 0:
            print("Goc toa do")
            return True
        elif self.x == 0: print("Truc tung")
        elif self.y == 0: print("Truc hoanh")
    def dist(self):
        return  (self.x * self.x + self.y * self.y)**0.5
    
a,b = map(int,input().split())
X = point_2D(a,b)
if X.kiemtra() == True: print("{0:.2f}".format(0))
else : print("{0:.2f}".format(X.dist()))