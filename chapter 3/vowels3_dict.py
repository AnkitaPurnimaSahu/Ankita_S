vowels = ['a','e','i','o','u']
word = input('Provide a word to search for vowel: ')
found = {}
# found['a'] = 0
# found['e'] = 0
# found['i'] = 0
# found['o'] = 0
# found['u'] = 0
for letter in word:
    if letter in vowels:
        #Dynamically initiates the dictionary, 
        # instead of giving a value to each of the vowels, 
        # now only those vowels will show up which have been initalized 
        # in case the 'if' condition is satisfied
        found.setdefault(letter,0)
        found[letter]+=1
for k,v in sorted (found.items()):
    print(k, 'was found',v,'times(s).')