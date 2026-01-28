try:
    age = int(input())
    if age < 0:
        raise ValueError
    print(2025 - age)
except ValueError:
    print("Tuoi khong hop le")
