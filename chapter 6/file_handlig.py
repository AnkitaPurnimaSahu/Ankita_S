# tasks = open('chapter 6\\todos.txt')
# for chore in tasks:
#     print(chore, end='')
# tasks.close()

with open('chapter 6\\todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')

# Notice anything missing? The call to close does not make an appearance.
# The with statement is smart enough to remember to call close on your behalf
# whenever its suite of code ends.