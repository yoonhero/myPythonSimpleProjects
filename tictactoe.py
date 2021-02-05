def start():
    print("Welcome to tictactoe")
    print(" -------")
    print("| 1 2 3 |")
    print("| 4 5 6 |")
    print("| 7 8 9 |")
    print(" -------")
    
def printthing(board):
    print("| ", board[1], " " ,board[2]," ",board[3], " |")
    print("| ", board[4], " " ,board[5]," ",board[6], " |")
    print("| ", board[7], " " ,board[8]," ",board[9], " |")
    return

def end(board):
    n = 0
    for c in board:
        if c != "-":
            n += 1
    return n

def condition(board, turn):
    for i in [1,4,7]:
        if board[i] == turn and board[i+1] == turn and board[i+2] == turn:
            return True
    for i in [1,2,3]:
        if board[i] == turn and board[i+3] == turn and board[i+6] == turn:
            return True
    if board[1] == turn and board[5] == turn and board[9] == turn:
        return True
    if board[3] == turn and board[5] == turn and board[7] == turn:
        return True
    return False
    
    
def numOrNot(num):
    if num.isdigit() :
        num = int(num)
    else: 
        return True
    
again = False
game_condition = True

def playerInput(board, turn):
    num = input("choose num: ")
    global again
    global game_condition
    if numOrNot(num) != True and int(num) < 10:
        num = int(num)
        if board[num] == "-":
            board[num] = turn
            printthing(board)
            again = False
            if condition(board, turn) == True:
                game_condition = False
                print("You are winner ", turn)
        else:
            print("please choose appropriate number not string. less than 10")
            again = True
    else:
        print("please choose appropriate number not string. less than 10")
        again = True
    

board = []
for i in range(0, 10):
    board.append("-")
#board = "-" * 10
turn = "O"
start()
again = False

while game_condition:
    
    print("Your turn ", turn)
    playerInput(board, turn)
        
    if again == False:    
        if turn == "O":
            turn = "X"
        else:
            turn = "O"
    if end(board) >= 9:
        print("the game is end")
        break