import pygame
from pygame.locals import *
from random import randrange

# initalize the pygame window

pygame.init()
clock = pygame.time.Clock()


length = 600 # length of window
width = 600 # width of window

display = pygame.display.set_mode((length, width))





block_size = 5 # size of each rectangle


def print_(grid): # prints a 2d array 
	for i in grid: 
		print(i)
		
def display_matrix(display,grid,blocksize): # displays a 2d array to the pygame window
	colors = {0:(255,255,255),1:(0,0,0)} # 1 represents a black pixel, 0 reps a white pixel
	for y in range(len(grid)): 
		for x in range(len(grid[y])):
			rect = pygame.Rect((x*block_size), (y*block_size), block_size, block_size) # creates a rectangle for every value of the 2d array
			pygame.draw.rect(display, colors[grid[x][y]], rect) # draws the rectangle to the screen

def create_grid(row,col): # function to create a 2d array with random 1s or 2s
	block_sizeult = []
	for i in range(col):
		block_sizeult.append([])
		for x in range(row):
			block_sizeult[-1].append(randrange(2))
	return block_sizeult

def empty_grid(row,col): # function to create a empty 2d array
	block_sizeult = []
	for i in range(col):
		block_sizeult.append([])
		for x in range(row):
			block_sizeult[-1].append(0)
	return block_sizeult


def count_neighbours(grid,x,y): # counts the 8 neighbours surronding a point in the 2d array
	sum = 0
	cols = len(grid)
	rows = len(grid[0])
	for i in range(-1,2):
		for j in range(-1,2):
			col = (x + i + cols) % cols
			row = (y + j + rows) % rows
			sum += grid[col][row]

	sum-=grid[x][y]
	return sum

grid = create_grid(int(length/block_size),int(width/block_size))

while True:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()

	new_grid = empty_grid(int(length/block_size),int(width/block_size))
	for col in range(len(grid)):
		for row in range(len(grid[col])):
			count = count_neighbours(grid,col,row)
			if grid[col][row] == 1 and count == 2 or count == 3:
				new_grid[col][row] = 1
			if grid[col][row] == 0 and count == 3:
				new_grid[col][row] = 1

	grid = new_grid.copy()
	#print(grid)
	display_matrix(display,grid,block_size)
	pygame.display.update()


