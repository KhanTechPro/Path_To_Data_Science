## Exercise 3: Print characters present at an even index number

word = input('Enter word: ')

print("Orginal String:", word)

size = len(word)

print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])