import random


def hangman():
    word = random.choice(['computer', 'airplane', 'elephant', 'earthquake',
                          'mother', 'flower', 'crazy', 'ocean', 'summer', 'popcorn'])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessMade = ''

    while len(word) > 0:
        main = ''

        for letter in word:
            if letter in guessMade:
                main = main + letter
            else:
                main = main + '_' + ' '
        if main == word:
            print(main)
            print('That is correct. You win!')
            break

        print('Guess the word:', main)
        guess = input()

        if guess in validLetters:
            guessMade = guessMade + guess
        else:
            print('Enter a valid character')
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print('9 turns left')
                print(' ------------ ')
            if turns == 8:
                print('8 turns left')
                print(' ------------ ')
                print('       O      ')
            if turns == 7:
                print('7 turns left')
                print(' ------------ ')
                print('       O      ')
                print('       |      ')
            if turns == 6:
                print('6 turns left')
                print(' ------------ ')
                print('       O      ')
                print('       |      ')
                print('      /       ')
            if turns == 5:
                print('5 turns left')
                print(' ------------ ')
                print('       O      ')
                print('       |      ')
                print('      / \     ')
            if turns == 4:
                print('4 turns left')
                print(' ------------ ')
                print('      \O      ')
                print('       |      ')
                print('      / \     ')
            if turns == 3:
                print('3 turns left')
                print(' ------------ ')
                print('      \O/     ')
                print('       |      ')
                print('      / \     ')
            if turns == 2:
                print('2 turns left')
                print(' ------------ ')
                print('      \O/|     ')
                print('       |      ')
                print('      / \     ')
            if turns == 1:
                print('1 turns left')
                print(' ------------ ')
                print('      \O/_|   ')
                print('       |      ')
                print('      / \     ')
            if turns == 0:
                print('0 turns left')
                print(' ------------ ')
                print('       O_|   ')
                print('      /|\     ')
                print('      / \     ')
                break

name = input('Please enter your name')
print('Welcome', name)
print('-----------------')
print('Try to guess the word in 10 tries or less')
hangman()
print()
