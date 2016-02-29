# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically

words = []

run = True

while run:
    word = input("Word: ")

    if word == "quit":
        run = False
    else:
        words.append(word)

for i in sorted(words):
    print(i, end=" ")