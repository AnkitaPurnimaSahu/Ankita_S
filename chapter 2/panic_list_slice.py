# This is how I did it
# phrase = "Don't panic!"
# plist = list(phrase)
# # print(phrase)
# # print(plist)
# part1 = plist[1:8:]
# print("plist[1:7:] - ",part1)
# part1.remove("'")
# print('''part1.remove("'") - ''',part1)
# part1.insert(2,part1.pop(3))
# print('''part1.insert(2,part1.pop(3))''',part1)
# #print(plist)
# part1.insert(-1,part1.pop())
# '''The above line of code executes from right to left.
# Therfore, first part1.pop() is executed which removes the last character 'a'
# then 'on tp' is left. From this -1 index would be 'p'
# as per insert() before -1, i.e. p, previously popped value i.e. 'a'
# woulbe be inserted.'''
# print("final part1 - ",part1)

#This is how the book did it
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase+''.join([plist[5],plist[4],plist[7],plist[6]])
print(plist)
print(new_phrase)