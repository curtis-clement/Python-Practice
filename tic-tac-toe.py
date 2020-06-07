import random

board = [' ' for x in range(10)]


def insertLetter(letter, position):
    board[position] = letter


def spaceFree(position):
    return board[position] == ' '


def showBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ')
    print('   |   |   ')


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def isWinner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))


def playerMove():
    run = True
    while run:
        move = input('Select a position betwen 1 and 9')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is taken!')
            else:
                print('Please enter a number between 1 and 9')
        except:
            print('Please type a number')


def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def computerMove():
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


def main():
    print('Welcome to the game!')
    showBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            showBoard(board)
        else:
            print('Sorry, you lose :(')
            break

        if not(isWinner(board, 'X')):
            move = computerMove()
            if move == 0:
                print(' ')
            else:
                insertLetter('O', move)
                print('The computer placed an O in space', move, ':')
                showBoard(board)
        else:
            print('You win!')
            break

    if isBoardFull(board):
        print('This game ends in a tie')


while True:
    x = input('Do you want to play again? (y/n)')
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('---------------------')
        main()
    else:
        break
