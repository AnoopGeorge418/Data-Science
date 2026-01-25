try:
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))

    result = num1 / num2
    print(result)

except ZeroDivisionError as e:
    print("Cannot divide by 0")

except ValueError as e:
    print("Invalid input")
    
