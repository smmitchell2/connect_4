from __future__ import print_function

def menu():
    print()
    print ("Welcome to Connect 4")
    print ("Choose versus are computer")
    print("1: Computer")
    print("2: Versus")
    print()

def createArray(size):
    return [None] * size

def createBoard():
    m = createArray(6)
    for r in range(0,6,1):
        m[r] = createArray(7)
    for r in range(0,6):
        for c in range(0,7):
            m[r][c] = '[O]'
    return m

def printBoard(m):
    for r in range(0,6):
        for c in range(0,7):
            print(m[r][c],end="")
        print()
    print(' 0  1  2  3  4  5  6')
    return



#def versus():

def choice1(colNum,board):
    rowNum = 5
    while rowNum >= 0:
        if board[rowNum][colNum] == '[O]':
            board[rowNum][colNum] = '[R]'
            return board
        rowNum = rowNum - 1
    return board

def choice2(colNum,board):
    rowNum = 5
    while rowNum >= 0:
        if board[rowNum][colNum] == '[O]':
            board[rowNum][colNum] = '[B]'
            return board
        rowNum = rowNum - 1
    return board

def checkDiagnol(board):
    winner = False
    for row in range(3):
        for col in range(4):
            if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]) and (board[row][col] != " "):
                winner = True
                return winner

    for row in range(5, 2, -1):
        for col in range(3):
            if (board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]) and (board[row][col] != " "):
                winner = True
                return winner

    return winner

def checkVertical(board):
    winner = False
    for col in range(6):
        for row in range(3):
            if (board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]) and (board[row][col] != " "):
                winner = True
                return winner
    return winner

def checkHorizontal(board):
    winner = False
    for row in range(6):
        for col in range(3):
            if (board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]) and (board[row][col] != " "):
                    winner = True
                    return winner
    return winner

def isGameOver(board):
    winner = False
    if checkDiagnol(board) == True:
        return True
    if checkVertical(board) == True:
        return True
    if checkHorizontal(board) == True:
        return True

def main():
    play = True
    menu()
    choice = int(input("Which choice? "))
    print()
    m = createBoard()
    printBoard(m)
    while play == True:
        winner = False
        print()
        colNum = int(input("Player 1 choose a row "))
        if colNum > 6:
            print ("Out of range choose number from 0-6")
            colNum = int(input("Which row? "))
        m = choice1(colNum,m)
        winner = isGameOver(m)
        if winner == True:
            print("Player 1 is the winner")
            printBoard(m)
            break
        printBoard(m)
        print()
        colNum = int(input("Player 2 choose a row "))
        if colNum > 6:
            print ("Out of range choose number from 0-6")
            colNum = int(input("Which row? "))
        m = choice2(colNum,m)
        winner = isGameOver(m)
        if winner == True:
            print("Player 2 is the winner")
            printBoard(m)
            break
        printBoard(m)

main()
