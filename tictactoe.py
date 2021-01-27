
import random as rd

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

num = 0
winner = None

def displayBoard():
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def currentPlayer(n):
    if n%2 == 0:
        return 'X'
    else:
        return 'O'


def playGame():

    global num
    
    displayBoard()
    print()
    toPlay = input("Do you want to play with the computer (Y/N) : ")

    while True:
        print()
        if toPlay.capitalize() == "Y":

            if currentPlayer(num) == "X":
                print(f'Current Player is "{currentPlayer(num)}"')
                playerInput = input("Enter Position from 1-9 : ")
                print()

                while playerInput not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    playerInput = input("Invalid Input. Enter Position from 1-9 : ")

                while board[int(playerInput)-1] != "-":
                    playerInput = input("Position already occupied. Choose a new one from 1-9   : ")

                board[int(playerInput)-1] = currentPlayer(num)
            else:
                playerInput = rd.randint(0, 8)
                while board[playerInput] != "-":
                    playerInput = rd.randint(0, 8)
                board[playerInput] = currentPlayer(num)
                print("Computer's Turn")
                print()
        elif toPlay.capitalize() == "N":
            print(f'Current Player is "{currentPlayer(num)}"')
            playerInput = input("Enter Position from 1-9 : ")
            print()
            while playerInput not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                playerInput = input("Invalid Input. Enter Position from 1-9 : ")
            while board[int(playerInput)-1] != "-":
                playerInput = input("Position already occupied. Choose a new one from 1-9   : ")
            board[int(playerInput)-1] = currentPlayer(num)
        else:
            print("Invalid Input. Try again !")
            break

        displayBoard()
        if checkGameOver():
            print()
            print("Game Over :)")
            print(f'Winner is : {winner}')
            print()
            break 
        elif num == 8 and winner == None:
            print()
            print("Game Over :)")
            print(f'Its a Tie !')
            print()
        num += 1

def checkGameOver():
    return checkWinner()

def checkWinner():

    global winner

    if rowWinner():
        winner = rowWinner()
        return True
    elif columnWinner():
        winner = columnWinner()
        return True
    elif diagonalWinner():
        winner = diagonalWinner()
        return True
    else:
        winner = None

def rowWinner():
    for n in range(0, 7, 3):
        if board[n] == board[n+1] == board[n+2] != "-":
            return board[n]

def columnWinner():
    for n in range(0, 3):
        if board[n] == board[n+3] == board[n+6] != "-":
            return board[n]

def diagonalWinner():
    for n in range(0, 1):
        if board[n] == board[n+4] == board[n+8] != "-":
            return board[n]
        elif board[n+2] == board[n+4] == board[n+6] != "-":
            return board[n]

playGame()
