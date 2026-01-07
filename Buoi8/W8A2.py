class date:
    def __init__(self,x,y,z):
        self.date = x
        self.month = y
        self.year = z
    def kiemtra(self):
        if self.year < 1 : return False
        else :
            if  1 > self.month or self.month > 12: return False
            elif self.month in [1, 3, 5, 7, 8, 10, 12]:
                if 1 > self.date or self.date > 31: return False
            elif self.month == 2:
                if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
                    if 1 > self.date or self.date > 29: return False
                elif 1 > self.date or self.date > 28: return False
            elif 1 > self.date or self.date > 30: return False
        return True
    def ngayke (self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            if self.date < 31:
                self.date += 1
                return print(str(self.date) + '/' + str(self.month) + '/' + str(self.year))
            elif self.month != 12:
                self.date = 1
                self.month += 1
                return print(str(self.date) + '/' + str(self.month) + '/' + str(self.year))
            else :
                self.date = 1
                self.month = 1
                self.year += 1
                return print(str(self.date) + '/' + str(self.month) + '/' + str(self.year))
        elif self.month == 2:
            if self.date < 28:
                    self.date += 1
                    return print(str(self.date) + '/' + str(self.month) + '/' + str(self.year))
            elif ((self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0) and self.date == 28 :
                self.date += 1
                return print(str(self.date) + '/' + str(self.month) + '/' + str(self.year))
            else :
                self.date = 1
                self.month += 1
                return print(str(self.date) + '/' + str(self.month) + '/' + str(self.year))
                    
        else:
            if self.date < 30:
                self.date += 1
                return print(str(self.date) + '/' + str(self.month) + '/' + str(self.year))
            else :
                self.date = 1
                self.month += 1
                return print(str(self.date) + '/' + str(self.month) + '/' + str(self.year))

a, b, c = map(int, input().split('/'))
X = date(a,b,c)
if X.kiemtra() == False: print("INVALID")
else: X.ngayke()
            