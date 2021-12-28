!pip install youtube_dl
import os
import youtube_dl
import re
import urllib.request
import requests
import time
from random import randint
!pip install ipython

def dad_joke():
    data = requests.get("https://icanhazdadjoke.com/",
                        headers={"Accept": "application/json"})
    data = data.json()
    return(data["joke"])


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print(f'your timer is up{home}')


def play_music(name):
    name = list(name)
    name = ["+" if x == " " else x for x in name]
    vid_url = (f"https://www.youtube.com/results?search_query={''.join(name)}")
    html = urllib.request.urlopen(vid_url)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    song_link = video_ids[0]
    path = os.getcwd()
    music_folder = os.path.join(path, "music")
    if os.path.exists(music_folder):
        music_folder = os.path.join(path, "music")
    else:
        os.mkdir(os.path.join(path, "music"))
        music_folder = os.path.join(path, "music")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(music_folder, "music.mp3"),
    }

    if len(os.listdir(music_folder)) != 0:
        os.remove(os.path.join(music_folder, "music.mp3"))
    else:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'https://www.youtube.com/watch?v={song_link}'])

    
           
            
home = input("what would you like me to call u?:  ")
want = input(f"{home}what can i do to help u(type help if you want to know what i can do) : ")
if want == "riddle" or want == "Riddle" or want == "RIDDLE":
    riddle = ["what goes up when rain comes down ?", "How many months of the year have 28 days?",
                "What has hands and a face, but can’t hold anything or smile?", " If you don’t keep me, I’ll break. What am I?"]
    num = randint(0, 3)
    print(riddle[num])
    solution = ["umbrella", "12", "clock", "promise."]
    answer = input("your answer pls ")
    if (answer == solution[num]):
        print(f"{home} your answer is correct")
    else:
        print(f"{home} your answer is wrong")
elif want == "joke" or want == "JOKE" or want == "Joke":
        print(dad_joke())
elif want == "game" or want == "Game" or want == "GAME":
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
                return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and
                bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le
                and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le
                and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le
                and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

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
elif want == "calculator" or want == "Calculator" or want == "CALCULATOR":
        x = float(input("enter a number: "))
        y = input("enter a opration: ")
        z = float(input("enter a numder: "))

        if y == "*":
            print("your answer is", x*z)
        elif y == "/":
            print("your answer is", x/z)
        elif y == "+":
            print("your answer is", x+z)
        elif y == "^":
            print("your answer is", x**z)

        else:
            print("your answer is", x-z)
elif want == "timer" or want == "Timer" or want == "TIMER":
        t = input("Enter the time in seconds: ")
        countdown(int(t))
elif want.lower() == "nick name":
        name = input(
            f"would you like to change your nick name (enter y for yes and n for no):(your name is currently {home}) ")
        if name == "y":
            new_name = input("your new you nick name: ")
            if new_name == home:

                print("it is alredy your nick name")
            else:
                print(f"okay your new nick name is {new_name} ")
        if name == "n":
            print(f"okay I will keep calling you {home}")
elif want.lower() == "music":
        name_song = input("music name")
        play_music(f"{name_song}")
elif want.lower() == "help":
        print ("type the following key words for the following\n music:to listen to some melodies \n joke:laugh your stress out\n game:to have fun and play some games with me\n nick to have you name changed to whaterver you want \n calculator:for a calculator i think n\nriddle if you want to test you mind \n timer to place a timer for how many ever seconds u want") 

else:
     print("sorry i cannot do that")

