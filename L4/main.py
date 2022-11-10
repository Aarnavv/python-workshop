from word_generator import generate

word = generate()
print(word)

word_show = []
for i in range(0, len(word)):
    word_show.append('_')

used_letters = ''

i = 0
while i < 7:
    print('-----------------------------------')
    print(word_show)
    print((7 - i), "lives left")
    letter = input("Guess a letter: ")

    # if the user-input letter has already been guessed before, the life is not used up
    if letter in used_letters:
        "Already guessed"
        continue

    used_letters += letter

    # If the user-input letter is present in the string, it enters all occurences of the letter

    if letter in word:
        for index in range(0, len(word_show)):
            if word[index] == letter:
                word_show[index] = letter
    else:
        i += 1
        print(letter, 'is not in the word')

    if '_' not in word_show:
        print(word_show)
        print("You won!")
        break
