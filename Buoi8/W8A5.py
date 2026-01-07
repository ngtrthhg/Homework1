class ShoppingCart:
    def __init__(self):
        self.cart = {}
    def add_new(self, x, y):
        self.cart[x] = y
    def remove_one(self, x):
        del self.cart[x]
    def kiemtra(self):
        if len(self.cart) == 0: return print("Giỏ rỗng")
        else : return print("Giỏ không rỗng")
    def tongtien(self):
        ans = 0
        for i in self.cart:
            ans += self.cart[i]
        return ans
    def hienthi(self):
        for i in self.cart:
            print (i,':',self.cart[i])
    def remove_all(self):
        self.cart = {}
        
X = ShoppingCart()
while True:
    A = list(map(str,input().split()))
    if A[0] == "yes" : break
    elif A[0] == '2': X.add_new(A[1], float(A[2]))
    elif A[0] == '3': X.remove_one(A[1])
    elif A[0] == '4': X.kientra()
    elif A[0] == '5': X.tongtien()
    elif A[0] == '6': X.hienthi()
    else : X.remove_all()
    print("Có muốn thoát khỏi chương trình không?")
    
        