# def search4vowels(word : str) -> set:
#     '''Return any vowels found in an supplied word'''
#     vowels = set('aeiou')
#     # word = input("Provide a word to search for vowels: ")
#     # found = vowels.intersection(set(word))
#     # for vowel in found:
#     #     print(vowel)
#     # return found
#     return vowels.intersection(set(word))


# def search4letters(phrase : str, letters : str = 'aeiou') -> set:
#     '''Return a set of the 'letters' found in 'phrase'.'''
#     return set(letters).intersection(set(phrase))
def search4vowels(word: str) -> set:
    '''Return any vowels found in a supplied word.'''
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    '''Return a set of the 'letters' found in 'phrase'.'''
    return set(letters).intersection(set(phrase))


# print(search4letters(letters='xyz',phrase='galaxy'))

# This is how I did it
# ch = input('Enter 1 for vowels search, Enter 2 for phrase search, Enter q to quit ')
# while True:
#     if ch=='1':
#         print(search4vowels(input('Enter a word: ')))
#         ch = input('Enter 1 for vowels search, Enter 2 for phrase search, Enter q to quit ')
#     elif ch=='2':
#         print(search4letters(input('Enter a phrase: '), input('Enter search letters: ')))
#         ch = input('Enter 1 for vowels search, Enter 2 for phrase search, Enter q to quit ')
#     elif ch=='q':
#         break
#     else:
#         print("Press 'Enter key again' as you have entered invalid input")
#         ch = input('Enter choice again (1, 2 or q)')