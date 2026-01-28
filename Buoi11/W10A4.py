try:
    a = int(input())
    b = int(input())

except ValueError:
    pass

else:
    print(a + b)

finally:
    print("Kết thúc chương trình.")
