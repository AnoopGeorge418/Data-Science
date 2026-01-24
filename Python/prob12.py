# ask the user for a number n
# print number from 1 to n
# print only number divisible by 3

n = input("Enter a number: ")

n = int(n)

for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)

