#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import random
PLAYER_STONE = 'O'
COMPUTER_STONE = 'X'

#게임에 관해 안내한다.


def printInfo():
	print("[Player-Computer Version]")
	print("틱택토(tic-tac-toe) 두 명이 번갈아가며 'O'와 'X'를 3×3 판에 써서 같은 글자를 가로, 세로, 혹은 대각선 상에 놓이도록 하는 놀이입니다.")
	print("플레이어는 'O', 컴퓨터는 'X'를 사용합니다.")
	print("위치 선택은 아래와 같이 키보드의 숫자 키패드를 이용하세요.")
	print("---------")
	print("| 7 8 9 |")
	print("| 4 5 6 |")
	print("| 1 2 3 |")
	print("---------")


#보드의 내용을 화면에 출력한다.
def drawBoard(board):
	print("---------")
	print("|", board[7], board[8], board[9], "|")
	print("|", board[4], board[5], board[6], "|")
	print("|", board[1], board[2], board[3], "|")
	print("---------")


#누가 먼저 시작할지 랜덤하게 정하고, 정해진 순서('O' 또는 'X')를 리턴한다.
def whoIsFirst():
	first = random.choice(['O', 'X'])

	if first == PLAYER_STONE:
		print("플레이어부터 시작합니다.")
	else:
		print("컴퓨터부터 시작합니다.")

	return first


#플레이어로부터 위치를 입력받는다.
def getPlayerMove(board, stone):
	while True:
		inData = input('위치를 선택하세요. ')
		if len(inData) == 1 and '1' <= inData <= '9':
			pos = int(inData)
			if board[pos] == '-':
				board[pos] = stone
				break
		print('잘못 선택하셨습니다. 비어있는 칸을 숫자로 입력하세요.')


#컴퓨터가 위치를 선택하게 한다.
def getComputerMove(board, stone):
    print('컴퓨터가 둡니다.')

    if board[5] == "-":
        board[5] = COMPUTER_STONE
        return

	#컴퓨터가 두면 이길 위치를 찾아둔다.
    for i in range(1, 10):
        if board[i] == '-':
            copyBoard = board[:]
            copyBoard[i] = COMPUTER_STONE
            if isWinner(copyBoard, COMPUTER_STONE):
                board[i] = COMPUTER_STONE
                return

	#플레이어가 두면 이길 위치를 찾아둔다.
    for i in range(1, 10):
        if board[i] == '-':
            copyBoard = board[:]
            copyBoard[i] = PLAYER_STONE
            if isWinner(copyBoard, PLAYER_STONE):
                board[i] = COMPUTER_STONE
                return
    #앞에서부터 빈자리를 찾아 둡니다.
    for i in range(1, 10):
        if board[i] == '-':
            board[i] = stone
            break   
	

#보드에 놓여진 돌의 개수를 리턴한다.
def numberOfStone(board):
	n = 0
	for c in board:
		if c != '-':
			n = n + 1
	return n


#보드에서 stone('O' 또는 'X')가 연속해서 3개 놓여졌는지 여부(True 또는 False)를 리턴한다.
def isWinner(board, stone):

	#가로 세 행 확인
	for i in [1, 4, 7]:
		if board[i] == stone and board[i + 1] == stone and board[i + 2] == stone:
			return True

	#세로 세 열 확인
	for i in [1, 2, 3]:
		if board[i] == stone and board[i + 3] == stone and board[i + 6] == stone:
			return True

	#대각선(오른쪽 위에서 왼쪽 아래)
	if board[1] == stone and board[5] == stone and board[9] == stone:
		return True

	#대각선(왼쪽 위에서 오른쪽 아래)
	if board[7] == stone and board[5] == stone and board[3] == stone:
		return True

	return False


#틱택토 1게임을 진행합니다.
def ticTacToe():

	#빈 틱택토 보드를 표현하기 위해서 '-'로 10개의 요소를 채운 리스트를 만듭니다.
	#위치 정보와 리스트의 인덱스를 일치시키기 위해 10개의 요소를 채우고, 이후에 맨 앞(인덱스 0) 요소는 사용하지 않습니다.
	tttBoard = ['-'] * 10
	drawBoard(tttBoard)

	currentStone = whoIsFirst()

	while True:
		if currentStone == PLAYER_STONE:
			getPlayerMove(tttBoard, PLAYER_STONE)
			drawBoard(tttBoard)

			if isWinner(tttBoard, PLAYER_STONE):
				print("축하합니다. 당신이 이겼어요!")
				return PLAYER_STONE

			currentStone = COMPUTER_STONE

		else:
			getComputerMove(tttBoard, COMPUTER_STONE)
			drawBoard(tttBoard)

			if isWinner(tttBoard, COMPUTER_STONE):
				print("아쉽군요. 컴퓨터가 이겼습니다.")
				return COMPUTER_STONE

			currentStone = PLAYER_STONE

		if numberOfStone(tttBoard) >= 9:
			print("비겼습니다.")
			return '-'


printInfo()

resultList = []

while True:
	result = ticTacToe()
	resultList.append(result)

	isContinued = input("한 게임 더 진행할까요?(y/n) ")
	if isContinued == 'n':
		break

print('\n[게임 전적]')
print(resultList.count(PLAYER_STONE), '승 ', resultList.count('-'), '무 ', resultList.count(COMPUTER_STONE), '패', sep='')
