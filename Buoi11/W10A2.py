my_list = list(map(int,input().split()))
try:
    print(my_list[len(my_list)])
except IndexError:
    print("Lỗi: Truy cập chỉ số sai (IndexError)")