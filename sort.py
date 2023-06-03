table = [['r', 'r', 'b', 'b'], ['b', 'b', 'r', 'r'],
         ['', '', '', ''], ['', '', '', '']]
moves = []

def colY(col):
    y = len(col)-1
    while y > -1 and col[y] == '':
        y = y-1
    return y

def current(x):
    col=table(x)
    y=colY(col)
    return col[y] if y>-1 else ''

def check_last():
    while len(last_move)<len(table):
        last_move = last_move.append(-1)

    for x in range(len(table)):
        l = last_move[x]; 
        if l==-1:
            continue
        
        
def move(x=None, lX=-1, last=''):
    if x == None:
        for dX in range(len(table)):
            okay = move(dX, lX, last)
            if okay != None:
                return okay
        return None

    # find the row:
    col = table[x]
    y = colY(col)
    print("y", col, y)
    if y == -1:
        return None

    for dX in range(len(table)):
        if dX == x:
            continue
        dCol = table[dX]
        dY = colY(dCol)
        if dY == len(dCol)-1:
            continue
        if dY > -1 and dCol[dY] != col[y]:
            continue
        if dX == lX and dCol[dY] == last:
            continue
        # swap and test:
        dY = dY+1
        dCol[dY] = col[y]
        col[y] = ''
        print(table)
        if all([len(set(x)) == 1 for x in table]):
            return f'{x}-{dX}'
        okay = move(None, x, dCol[dY])
        if okay != None:
            return f'{x}-{dX}, {okay}'
        col[y] = dCol[dY]
        dCol[dY] = ''
    return None

def reorder_table():
    for x in range(len(table)):
          print(table[x])

if __name__ == "__main__":
    print(move())
