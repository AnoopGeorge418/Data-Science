word = input("Enter: ")
vowels = [ 'a', 'e', 'i', 'o', 'u' ]

count = 0

for i in word.lower():
    if i in vowels:
        count += 1
        
        
print(count)


