import os
from t48Bot import *
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

board = [[0 for j in range(4)]for i in range(4)]

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if len(message.content)!=1:
		return
		
	inp = message.content.lower()
	global board
	if inp in ['w','a','s','d']:
		board = move(board,inp)
		await message.channel.send(disc_print_board(board))
		
		if board == 0:
			await message.channel.send("Game Over")
			board = clear_board()
		
	
	elif inp=='r':
		board = clear_board()
		await message.channel.send(disc_print_board(board))
	



client.run(TOKEN)

