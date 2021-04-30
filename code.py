import random

home = input("enter your name: ")
want = input(f"{home} what do you want: ")
if want == "riddle" or want == "Riddle" or want == "RIDDLE":
    riddle = ["what goes up when rain comes down ?", "How many months of the year have 28 days?",
              "What has hands and a face, but can’t hold anything or smile?", " If you don’t keep me, I’ll break. What am I?"]
    num = random.randint(0, 3)
    print(riddle[num])
    solution = ["umbrella", "12", "clock", "promise."]
    answer = input("your answer pls ")
    if (answer == solution[num]):
        print(f"{home} your answer is correct")
    else:
        print(f"{home} your answer is wrong")
if want == "joke" or want == "JOKE" or want == "Joke":
    import requests

    params = {"Accept: application/json"}

    data = requests.get("https://icanhazdadjoke.com/",
                        headers={"Accept": "application/json"})

    data = data.json()

    print(data["joke"])
if want == "games" or want == "Games" or want == "GAMES" or want == ("game") or want == ("Game") or want == ("GAME"):
    game = input("rps or tictactoe: ")
    if game == "tictactoe":
        board = [' ' for x in range(10)]

        def insertLetter(letter, pos):
            board[pos] = letter

        def spaceIsFree(pos):
            return board[pos] == ' '

        def printBoard(board):
            print('   |   |')
            print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
            print('   |   |')

        def isWinner(bo, le):
            return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

        def playerMove():
            run = True
            while run:
                move = input(
                    'Please select a position to place an \'X\' (1-9): ')
                try:
                    move = int(move)
                    if move > 0 and move < 10:
                        if spaceIsFree(move):
                            run = False
                            insertLetter('X', move)
                        else:
                            print('Sorry, this space is occupied!')
                    else:
                        print('Please type a number within the range!')
                except:
                    print('Please type a number!')

        def compMove():
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

        def selectRandom(li):
            import random
            ln = len(li)
            r = random.randrange(0, ln)
            return li[r]

        def isBoardFull(board):
            if board.count(' ') > 1:
                return False
            else:
                return True

        def main():
            print('Welcome to Tic Tac Toe!')
            printBoard(board)

            while not(isBoardFull(board)):
                if not(isWinner(board, 'O')):
                    playerMove()
                    printBoard(board)
                else:
                    print('Sorry, O\'s won this time!')
                    break

                if not(isWinner(board, 'X')):
                    move = compMove()
                    if move == 0:
                        print('Tie Game!')
                    else:
                        insertLetter('O', move)
                        print('Computer placed an \'O\' in position', move, ':')
                        printBoard(board)
                else:
                    print('X\'s won this time! Good Job!')
                    break

            if isBoardFull(board):
                print('Tie Game!')

        while True:
            answer = input('Do you want to play again? (Y/N)')
            if answer.lower() == 'y' or answer.lower == 'yes':
                board = [' ' for x in range(10)]
                print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                main()
            else:
                break
    if game == "rps":
        from random import randint
    y = 'y'

    while y != 'n':

        x = randint(1, 3)
        print("1=rock,2=paper,3=sis")
        man = int(input("enter a number between 1 and 3 : "))

        if man == 1:
            print("you choose rock")
        elif man == 2:
            print("you choose paper")
        else:
            print("you choose sis")

        if x == 1:
            print("computer choose rock")
        elif x == 2:
            print("computer choose paper")
        else:
            print("computer choose sis")

        if x == man:
            print("draw")
        elif man == 1 and x == 3:
            print("man won")
        elif man == 2 and x == 1:
            print("man won ")
        elif man == 3 and x == 2:
            print("man won")
        else:
            print("computer won")

        y = input("Would you like to play agian? y/n: ")
if want == "calculator" or want == "Calculator" or want == "CALCULATOR":
    x=int(input("enter a number: "))
    y=input("enter a opration: ")
    z=int(input("enter a numder: "))

    if y=="*":   
        print("your answer is", x*z)
    elif y=="/":
        print("your answer is", x/z)
    elif y=="+":
        print("your answer is", x+z)
    elif y=="^":
        print("your answer is", x**z)

    else:
        print("your answer is",x-z)
             
