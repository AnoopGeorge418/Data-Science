# 2 numbers
# compare them
# print which number is bigger and is equal

num1 = input("Number 1: ")
num2 = input("Number 2: ")

num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    print("First is greater")
elif num1 < num2:
    print("Second is greater")          
else: 
    print("Both are equal")
