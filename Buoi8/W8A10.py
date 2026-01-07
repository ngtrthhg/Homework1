import bisect

class Book:
    def __init__(self, t, a, y):
        self.t = t
        self.a = a
        self.y = y
class Library:
    def __init__(self):
        self.author = []
        self.year = []
    def add(self, x):
        self.author.append(x.a)
        self.year.append(x.y)
    def count_by_year(self, x):
        self.year.sort()
        print(bisect.bisect_right(self.year, x) - bisect.bisect_left(self.year, x))
    def count_by_author(self, x):
        self.author.sort()
        print(bisect.bisect_right(self.author, x) - bisect.bisect_left(self.author, x))

n = int(input())
L = Library()
while n:
    n -= 1
    a, b = map(str,input().split())
    if a == "ADD":
        x, y, z = b.split(';')
        L.add(Book(x, y, z))
    elif a == "COUNT": L.count_by_author(b)
    elif a =="COUNTYEAR": L.count_by_year(b)

    