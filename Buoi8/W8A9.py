class Student:
    def __init__(self, x):
        self.name = x
        self.list = {}
        self.a = 0
    def add_score(self, x, y):
        self.list [x] = y
    def avg(self):
        ans = 0
        for i in self.list:
            ans += self.list[i]
        self.a = ans/len(self.list)
        return self.a
    def rank(self):
        if self.a >= 8 : return "Excellent"
        elif self.a >= 6.5: return "Good"
        elif self.a >= 5: return "Average"
        return "Poor"

x = input()
X = Student(x)
n = int(input())
while n:
    n -= 1
    a, b = map(str,input().split())
    X.add_score(a, float(b))
print(x, "{0:.2f}".format(X.avg()), X.rank()) 