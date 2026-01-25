try:
    with open("test.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError as e:
    print("File not found")
else:
    print("Data read")
finally:
    print("Done")

