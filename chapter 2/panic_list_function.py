phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist.pop(0) #removes 'd'
for i in range(4):
    plist.pop() #removes the last four objects
plist.remove("'")
#ont pa
# ch1_a = plist.pop(5)
# ch2_p = plist.pop(4)
# ch3_ = plist.pop(3)
# plist.insert(2,ch3_)
# plist.extend([ch1_a, ch2_p])
plist.extend([plist.pop(5), plist.pop(4)])
plist.insert(2,plist.pop(3))
new_phrase = ''.join(plist) #this line takes the list and turns it back into a string
print(plist)
print(new_phrase)