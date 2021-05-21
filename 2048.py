from t48 import *
import random	
	



inp = "j"
while inp!="q":
	inp = input()
	if inp=="a":
		board = move(board, 4)
	if inp=="w":
		board = move(board, 1)
	if inp=="s":
		board = move(board, 3)
	if inp=="d":
		board = move(board, 2)
		
	print_board(board)





