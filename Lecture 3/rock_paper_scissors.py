import time
import random
import sys

moves = ['rock', 'paper', 'scissors']

human_score = 0
computer_score = 0

def randomMove():
    choice = random.randint(0, 2)
    choice = moves[choice]
    return choice

def whoWon(player1, player2):
    global human_score
    global computer_score

    player1 = moves.index(player1.lower())
    player2 = moves.index(player2.lower())

    if (player1 == player2):
        print('Tie! Pick a move again.')
        play()
    elif(player1 == (player2 + 1) % len(moves)):
        print(name, 'won!')
        human_score = human_score + 1
    else:
        print('Computer won!')
        computer_score = computer_score + 1

def scores():
    print(name + ':', human_score)
    print('Computer:', computer_score)
    print()

def play():
    #Getting choice
    while True:
        human = input('Move: ').strip()
        if human.lower() in moves:
            break
        elif human.lower() in ['exit', 'quit', 'stop', 'bye']:
            sys.exit()
        print('Enter a valid move!')
    print()

    time.sleep(0.5)

    #Countdown
    for i in moves:
        print(i.capitalize())
        time.sleep(0.5)
    print()

    #Results
    print(name, 'chose:', human)
    computer = randomMove()
    print('Computer chose:', computer)
    winner = whoWon(human, computer)
    print()

    #Scores
    scores()
    
    #Play again?
    while True:
        replay = input('Do you want to play again?')
        if replay.lower() in ['y', 'yes', 'yup', 'yeah']:
            print()
            play()
        elif replay.lower() in ['n', 'no', 'nope', 'nah', 'bye']:
            sys.exit('Goodbye :)')
        else:
            print('Please enter a valid response.')

#Starting game
print('Welcome to Rock Paper Scissors.')
time.sleep(0.5)
name = input('Name: ').strip()
print()

play()