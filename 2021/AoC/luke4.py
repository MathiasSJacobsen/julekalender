def luke4silver(lines):
    numbers = [int(e) for e in lines[0].split(',')]
    boards = []
    board = []


    for e in lines[2:]:
        e = e.split()
        if e == []:
            boards.append(board)
            board = []
        else:
            board.append([int(i) for i in e])
    boards.append(board)

    nrOfBoards = len(boards)

    for num in numbers:
        for board in boards:
            for y in range(len(board)):
                for x in range(len(board[y])):
                    if board[y][x] == num:
                        board[y][x] = None

            
            if verifyBoardHori(board) or verifyBoardVert(board):
                nrOfBordsGood = 0 
                for tboard in boards:
                    if verifyBoardHori(tboard) or verifyBoardVert(tboard):
                        nrOfBordsGood += 1
                        if nrOfBordsGood == nrOfBoards:
                            sumOfNotNull = 0
                            for p in board:
                                for i in p:
                                    if i != None:
                                        sumOfNotNull += i
                                    
                            return sumOfNotNull * num
                #sumOfNotNull = 0
                #for p in board:
                 #   for i in p:
                  #      if i != None:
                   #         sumOfNotNull += i
                        
                #return sumOfNotNull * num

    
    print(verifyBoardVert(boards[0]))


def verifyBoardHori(board):
    for i in range(5):
        if board[i][0] == None and board[i][1] == None and board[i][2] == None and board[i][3] == None and board[i][4] == None:
            return True
    return False

def verifyBoardVert(board):
    for i in range(5):
        if board[0][i] == None and board[1][i] == None and board[2][i] == None and board[3][i] == None and board[4][i] == None:
            return True
    return False


if __name__ == '__main__':
    file = open('luke4silver.txt')
    b = luke4silver(file.readlines())
    print(b)