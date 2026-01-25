word = input("Enter a word: ")

characters = {}

for i in word:
    if i in characters:
        characters[i] += 1
    else:
        characters[i] = 1

print(characters)

