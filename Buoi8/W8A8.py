class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.x = balance
    def deposit(self, a):
        self.x += a
    def withdraw(self, a):
        self.x -= a
    def out(self):
        print("{0:.2f}".format(self.x))

a, b = map(str,input().split())
X = BankAccount(a, int(b))
n = int(input())
while n :
    n -= 1
    x, y = map(str,input().split())
    if x == "DEPOSIT": X.deposit(int(y))
    else: X.withdraw(int(y))
X.out()
