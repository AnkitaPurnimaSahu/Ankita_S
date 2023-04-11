#how I did it
# vowels = ['a','e','i','o','u']
# word = input("Enter the word: ")
# found = []
# for letter in word:
#     if letter in vowels and letter not in found:
#         found = [letter]
#         print(letter)

#how the books did it
vowels = ['a','e','i','o','u']
word = input("Enter the word: ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)