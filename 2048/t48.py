import random
board = [[0 for j in range(4)]for i in range(4)]

def print_board(board):
	for i in range(4):
		for j in range(4):
			print(board[i][j],end = ' ')
		print()

def transpose(board):
	temp = [[0 for j in range(4)]for i in range(4)]
	for row in range(4):
		for col in range(4):
			temp[col][row] = board[row][col]
	return temp

def scan_board(board):
	for i in range(4):
		line = input()
		board[i] = line.split(" ")
		board[i] = [int(i) for i in board[i]]
		
		
def combine(line):
	temp = []
	for i in line:
		if i!=0:
			temp.append(i)
	
	"""adds filler 0's"""
	for i in range(4-len(temp)):
		temp.append(0)
	line = temp
	
	
	temp = []
	c = 0
	while c<3:
		cur = line[c]
		nxt = line[c+1]
		if cur==nxt:
			temp.append(2*cur)
			c += 1
		else:
			if cur!=0:
				temp.append(cur)
		c += 1
		
	if (line[3]!=0) and (c==3):
		temp.append(line[3])
	
	for i in range(4-len(temp)):
		temp.append(0)
	line = temp	
	temp = []
	
	return line

def add_block(board):
	zeroes = []
	for row in range(4):
		for col in range(4):
			if board[row][col]==0:
				zeroes.append((row,col))
	if len(zeroes)==0:
		return 0
	
	
	block = zeroes[random.randint(0,len(zeroes)-1)]			#pick empty
	board[block[0]][block[1]] = 2							#put 2 on the empty
	zeroes = []	
	return 1						


def move(board, di):
	#1up   2right    3down    4left
	if di=='a':
		for i in range(4):
			board[i] = combine(board[i])
	
	if di=='d':
		for i in range(4):
			board[i][::-1] = combine(board[i][::-1])
	
	if di=='w':
		board = transpose(board)
		board = move(board, 'a')
		board = transpose(board)
	if di=='s':
		board = transpose(board)
		board = move(board, 'd')
		board = transpose(board)
	
	if add_block(board)==1:
		return board
	else:
		return 0


directions = {"w":1, "d":2, "s":3, "a":4}
inp = ""
while inp!="q":
	inp = input()
	if inp in ['w','a','s','d']:
		board = move(board,inp)
	
		if board==0:
			print("Game Over")
			break
	
		print_board(board)

