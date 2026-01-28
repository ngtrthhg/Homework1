try:
    filename = input().strip().lower()

    if not (filename.endswith(".txt") or filename.endswith(".zip")):
        raise ValueError

    print("Doc file thanh cong")

except ValueError:
    print("File khong hop le")
