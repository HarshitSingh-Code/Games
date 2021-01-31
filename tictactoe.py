
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
                board[computerMove()] = currentPlayer(num)
                print("Computer's Turn")
                print()
        elif toPlay.capitalize() == "N":
            print(f'Current Player is "{currentPlayer(num)}"')
            playerInput = input("Enter Position from 1-9 : ")
            print()
            while playerInput not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                playerInput = input("Invalid Input. Enter Position from 1-9 : ")
            while board[int(playerInput)-1] != "-":
                playerInput = input("Position already occupied. Choose a new one from 1-9 : ")
            board[int(playerInput)-1] = currentPlayer(num)
        else:
            print("Invalid Input. Try again !")
            break

        displayBoard()
        if checkGameOver(board):
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
            break
        num += 1

def checkGameOver(boards):
    return checkWinner(boards)

def checkWinner(boards):

    global winner

    if rowWinner(boards):
        winner = rowWinner(boards)
        return True
    elif columnWinner(boards):
        winner = columnWinner(boards)
        return True
    elif diagonalWinner(boards):
        winner = diagonalWinner(boards)
        return True
    else:
        winner = None

def rowWinner(boards):
    for n in range(0, 7, 3):
        if boards[n] == boards[n+1] == boards[n+2] != "-":
            return board[n]

def columnWinner(boards):
    for n in range(0, 3):
        if boards[n] == boards[n+3] == boards[n+6] != "-":
            return boards[n]

def diagonalWinner(boards):
    for n in range(0, 1):
        if boards[n] == boards[n+4] == boards[n+8] != "-":
            return boards[n]
        elif boards[n+2] == boards[n+4] == boards[n+6] != "-":
            return boards[n]

def computerMove():
    possibleMoves = [x for x, value in enumerate(board) if value == "-" and x!=0]
    move = 0

    for x in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = x
            if checkGameOver(boardCopy):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [0, 2, 6, 8]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = rd.choice(cornersOpen)
        return move
    
    if 4 in possibleMoves:
        move = 4
        return move
    
    edgesOpen = []
    for i in possibleMoves:
        if i in [0, 2, 6, 8]:
            edges.append(i)
    if len(edgesOpen) > 0:
        move = rd.choice(edgesOpen)
    
    return move

if __name__ == "__main__":
    playGame()
