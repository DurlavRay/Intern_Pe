import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(6):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(7):
            if(gameBoard[x][y] == "🔵"):
                print("",gameBoard[x][y], end=" |")
            elif(gameBoard[x][y] == "🔴"):
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyTurn(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

turnCounter = 0
while True:
    printGameBoard()
    columnLetter = input("Player " + str(turnCounter % 2 + 1) + ", choose a column (A-G): ").upper()
    if columnLetter in possibleLetters:
        column = possibleLetters.index(columnLetter)
        for i in range(5, -1, -1):
            if gameBoard[i][column] == "":
                modifyTurn((i, column), "🔵" if turnCounter % 2 == 0 else "🔴")
                turnCounter += 1
                break
    else:
        print("Invalid column. Please choose a column between A and G.")

    # Check win condition (not implemented yet)

    # Check draw condition (not implemented yet)