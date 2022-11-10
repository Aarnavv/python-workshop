import random

words = []

# for _ in range(0, 5):
#     words.append([input("Enter word: "), input("Enter hint: ")])


words = ['awkward', 'awesome', 'jazz', 'hangman', 'quiz']


def generate():
    i = random.randint(0, 4)
    return words[i]
