try:
    num1 = int(input("Number 1: "))
    print(num1)

except ValueError as e:
    print("Invalid input")
else:
    print("Conversion Successful")
