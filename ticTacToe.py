board = [' '  for i in range(3)]
board = [board.copy() for i in range(3)]

def printboard(board):
    ch = ' | '
    print('Board: ')
    for i in range(2):
        print(ch.join(board[i]))
        print('_'*10, end='\n\n')
    print(ch.join(board[2]))

def check(board):
    for i in range(3):
        s,t = '',''
        for j in range(3):
            s+=board[i][j]
            t+=board[j][i]
        if s == 'XXX' or t == 'XXX':
            return 1
        if s == 'OOO' or t == 'OOO':
            return -1
    s, t = '', board[0][2] + board[1][1] + board[2][0]
    for i in range(3):
        s+=board[i][i]
    if s == 'XXX'or t == 'XXX':
        return 1
    if s == 'OOO' or t == 'OOO':
        return -1
    return 0

def end_state(board):
    for l in board:
        for ch in l:
            if ch == ' ':
                return False
    return True

def is_valid(x, y):
    if x <= 0 or x > 3 or y <= 0 or y > 3:
        print('Error: Please enter valid co-ordinates')
        return False
    if board[x-1][y-1] != ' ':
        print(f'Error: Cell {x} {y} is already filled.')
        return False
    return True

def minmax(board, flag, level):
    if end_state(board) == True or check(board) != 0: # Base Case
        return check(board)
    if flag == 0:
        rval = 10
        d = dict()
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    d[(i,j)] = minmax(board, 1, level+1)
                    rval = min(rval, d[(i,j)])
                    board[i][j] = ' '
        if level == 0:
            for k,v in d.items():
                if v == rval:
                    board[k[0]][k[1]] = "O"
                    break
        return rval
    else:
        rval = -10
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    rval = max(rval, minmax(board, 0, level + 1))
                    board[i][j] = ' '
        return rval


if __name__ == '__main__':
    print('Welcome to Tic Tac Toe')
    print('You will be playing first. Enter the co-ordinates of your X. (Ex: Centre is 2 2)')
    for i in range(5):
        printboard(board)
        x,y = map(int,input().split())
        while is_valid(x, y) == False:
            x,y = map(int,input().split())
        board[x-1][y-1] = 'X'
        minmax(board,0,0)
        if check(board) == -1:
            print('I won! Nothing new for me!')
            break
        elif check(board) == 1:
            print('Impossible.')
        elif end_state(board) == 1:
            print('Draw')
            break

        
