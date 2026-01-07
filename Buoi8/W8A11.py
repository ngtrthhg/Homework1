import math

class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def mul_vec(self, a):
        multi = (self.y * a.z - self.z * a.y, self.z * a.x - self.x * a.z, self.x * a.y - a.x * self.y)
        self.x = multi[0]
        self.y = multi[1]
        self.z = multi[2]

A = list(map(float,input().split()))
B = list(map(float,input().split()))
C = list(map(float,input().split()))
D = list(map(float,input().split()))

AB = vector(A[0] - B[0], A[1] - B[1], A[2] - B[2])
AC = vector(A[0] - C[0], A[1] - C[1], A[2] - C[2])
BC = vector(B[0] - C[0], B[1] - C[1], B[2] - C[2])
BD = vector(B[0] - D[0], B[1] - D[1], B[2] - D[2])

AB.mul_vec(AC)
BC.mul_vec(BD)
mauso = ((AB.x * AB.x + AB.y * AB.y + AB.z * AB.z)*(BC.x * BC.x + BC.y * BC.y + BC.z * BC.z)) ** 0.5
tuso = AB.x * BC.x + AB.y * BC.y + AB.z * BC.z
if tuso < 0: tuso *= -1
ans  = math.acos(tuso/mauso) * 180 / math.pi
print("{0:.2f}".format(ans))

