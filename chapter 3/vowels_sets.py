# vowels = ['a','e','i','o','u']
vowels = set('aeiou')
word = input('Provide a word to search for vowels: ')
# found = []
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# for vowel in found:
#     print(vowel)
# common_i = set(vowels).intersection(set(word))
common_i = vowels.intersection(set(word))
print(common_i)