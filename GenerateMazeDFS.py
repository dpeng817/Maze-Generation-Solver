import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import argparse

#given length and width, generate maze with random depth-first walks
def generate_maze(length,width):
	#represents a single cell in maze
	#directions represent 'walls':0 means wall is up, false means cell is not visited
	#generate full maze of walled cells
	maze=generate_blank_maze(length,width)
	row=0#represent row in grid of maze
	col=0#represent column in grid of maze
	stack=[]#stores locations we have visited but not backtracked to
	stack.append([row,col])#always start at origin pt (0,0) for convenience's sake

	while(stack):
		maze[row][col]['visited']=True#mark current location as visited
		validMoves=[]
		#if moving up is still on maze, and that location has not yet been visited
		if(row>0 and maze[row-1][col]['visited']==False):
			validMoves.append('up')
		if(col>0 and maze[row][col-1]['visited']==False):
			validMoves.append('left')
		if(row<length-1 and maze[row+1][col]['visited']==False):
			validMoves.append('down')
		if(col<width-1 and maze[row][col+1]['visited']==False):
			validMoves.append('right')
		#if there is a valid location to go from here, 
		#add to stack of visited nodes and continue forward by proper increment
		if len(validMoves):
			stack.append([row,col])
			nextMove=random.choice(validMoves)
			
			if nextMove=='up':
				maze[row][col]['up']=1#remove wall to up, as it has been visited (or will be)
				row=row-1#move up
				maze[row][col]['down']=1#remove wall on next square
			if nextMove=='down':
				maze[row][col]['down']=1#remove wall to up, as it has been visited (or will be)
				row=row+1#move up
				maze[row][col]['up']=1
			if nextMove=='left':
				maze[row][col]['left']=1#remove wall to up, as it has been visited (or will be)
				col=col-1#move up
				maze[row][col]['right']=1
			if nextMove=='right':
				maze[row][col]['right']=1#remove wall to up, as it has been visited (or will be)
				col=col+1#move up
				maze[row][col]['left']=1
		#otherwise, dead end has been reached
		else:
			row,col=stack.pop()
	maze[0][0]['up']=1
	maze[length-1][width-1]['right']=1
	generate_image(maze,length,width)


#used image generation algorithm found on wikipedia
def generate_image(maze,length,width):
	#given finished maze, generate image
	#generate image 10x the size of the actual maze for viewing purposes
	image = np.zeros((length*10,width*10), dtype=np.uint8)
	for row in range(0,length):
		for col in range(0,width):
			cellData=maze[row][col]
			for i in range(10*row+1,10*row+9):
				image[i,range(10*col+1,10*col+9)] = 255
				if cellData['left']==1:
					image[range(10*row+1,10*row+9),10*col] = 255
				if cellData['up']==1:
					image[10*row,range(10*col+1,10*col+9)] = 255
				if cellData['right']==1:
					image[range(10*row+1,10*row+9),10*col+9] = 255
				if cellData['down']==1:
					image[10*row+9,range(10*col+1,10*col+9)] = 255
	# Display the image
	plt.imshow(image, cmap = cm.Greys_r, interpolation='none')
	plt.show()

def generate_blank_maze(length,width):
	result=[]
	for r in range(0,length):
		result.append([])
		for c in range(0,width):
			result[r].append(
				{
	'left':0,
	'right':0,
	'up':0,
	'down':0,
	'visited':False
	}
	)
	return result


parser=argparse.ArgumentParser(description='get dimensions')
parser.add_argument(
	'-l',
	'--length',
	dest='length',
	required=True,
	metavar='INT>0',
	type=str,
	help='length of maze to be created.'
	)
parser.add_argument(
	'-w',
	'--width',
	dest='width',
	required=True,
	metavar='INT>0',
	type=str,
	help='width of maze to be created.'
	)
args=parser.parse_args()
if args.length and args.width:
	generate_maze(int(args.length),int(args.width))
else:
	print('Please give a valid length and width.')

