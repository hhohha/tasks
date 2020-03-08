def displayChar(n):
    if n == 0:
        return ' '
    elif n == 1:
        return 'X'
    else:
        return 'O'
  
 
def printBoard (board):
    colCnt = len(board[0])
    
    for row in board:
        print(' ---' * colCnt + '\n' + '|', end='')
        for item in row:
            print(' ' + displayChar(item) + ' |', end='')
            
        print()
            
    print(' ---' * colCnt)

  
def isWinnerRow(board):
    for row in board:
        firstInRow = row[0]
        if firstInRow == 0:
            continue
        
        winFound = True
        for item in row:
            if firstInRow != item:
                winFound = False
                break
            
        if winFound:    
            return True    
            
    return False


def isWinnerCol(board):
    j = 0
    while j < len (board[0]):
        firstInRow = board [0][j]
        i = 0
        if firstInRow != 0:
            while i < len (board):
                if firstInRow != board [i][j]:
                    break
                i += 1
            if i == len (board):
                return True
        j += 1
    return False


def isWinnerDiag (board):
    i = 1
    firstInRow = board [0][0]
    
    if firstInRow != 0:
        while i < len (board):
            if firstInRow != board [i][i]:
                break
            i += 1
        if i == len (board):
            return True

    lastInRow = board [-1][0]
    i = 1
    
    if lastInRow != 0:
        while i < len(board):
            if lastInRow != board [-1 - i][i]:
                break
            i += 1
        if i == len (board):
            return True

    return False

def isWinner(board):
    if isWinnerRow(board) or isWinnerCol(board) or isWinnerDiag(board):
        return True
    else:
        return False
    
def areCoordsValid(board, x, y):
    if x >= len(board) or y >= len(board):
        return False
    
    if board[x][y] == 0:
        return True
    else:
        return False
 
 
board = [[0,0,0], [0,0,0], [0,0,0]]
rnd = 0
curPlayer = 1

while not isWinner(board) and rnd < 9:
    printBoard(board)
    
    command = input('\nwhere do you play?\n')
    
    
    
    if command == 'save':
        saveGame(board, curPlayer, rnd)
        continue
    if command == 'load':
        board, curPlayer, rnd = loadGame()
        continue
    
    
    
    x = int(coords[0])
    y = int(coords[1])
    
    if not areCoordsValid(board, x ,y):
        print('bad coordinates')
        continue
    
    board[x][y] = curPlayer
    
    rnd += 1
    if curPlayer == 1:
        curPlayer = 2
    else:
        curPlayer = 1
        
printBoard(board)

