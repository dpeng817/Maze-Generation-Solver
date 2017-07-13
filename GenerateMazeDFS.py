import random
import numpy
import scipy.misc as smp

#given length and width, generate maze with random depth-first walks
def generate_maze(length,width):
	#represents a single cell in maze
	#directions represent 'walls':0 means wall is up, false means cell is not visited
	blankCell={
	'left':0,
	'right':0,
	'up':0,
	'down':0,
	'visited':False
	}
	#dictionary to represent increments for various movements
	nextLocation={
	'up':[-1,0],
	'down':[1,0],
	'left':[0,-1],
	'right':[0,1]
	}
	#generate full maze of walled cells
	maze=[[blankCell]*width for i in range(length)]
	row=0#represent row in grid of maze
	col=0#represent column in grid of maze
	stack=[]#stores locations we have visited but not backtracked to
	stack.append([row,col])#always start at origin pt (0,0) for convenience's sake

	while(stack):
		maze[row][col]['visited']=True#mark current location as visited
		validMoves=[]
		#if moving up is still on maze, and that location has not yet been visited
		if(row-1>0 and maze[row-1][col]['visited']==False):
			validMoves.append('up')
		if(col-1>0 and maze[row][col-1]['visited']==False):
			validMoves.append('left')
		if(row+1<length-1 and maze[row+1][col]['visited']==False):
			validMoves.append('down')
		if(col+1<width-1 and maze[row][col+1]['visited']==False):
			validMoves.append('right')
		#if there is a valid location to go from here, 
		#add to stack of visited nodes and continue forward by proper increment
		if validMoves:
			stack.append([row,col])
			nextMove=random.choice(validMoves)
			
			if nextMove=='up':
				maze[row][col]['up']=1#remove wall to up, as it has been visited (or will be)
				row=row-1#move up
			elif nextMove=='down':
				maze[row][col]['up']=1#remove wall to up, as it has been visited (or will be)
				row=row+1#move up
			elif nextMove=='left':
				maze[row][col]['left']=1#remove wall to up, as it has been visited (or will be)
				col=col-1#move up
			elif nextMove=='right':
				maze[row][col]['left']=1#remove wall to up, as it has been visited (or will be)
				col=col+1#move up
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
	image=numpy.zeros((length*10,width*10),dtype='i,i,i')
	for row in range(0,length):
		for col in range(0,width):
			space=maze[row][col]#data for individual space in maze
			for pixelRow in range(row*10+1,row*10+9):
				image[pixelRow,range(10*col+1,10*col+9)]=255,255,255#mark as white
				if space['up']==1:
					image[10*row,range(10*col+1,10*col+9)] = 255,255,255
				if space['down']==1:
					image[10*row+9,range(10*col+1,10*col+9)] = 255,255,255
				if space['left']==1:
					image[range(10*row+1,10*row+9),10*col] = 255,255,255
				if space['right']==1:
					image[10*row,range(10*col+1,10*col+9)] = 255,255,255
	for row in image:print(image)
	generatedImage=smp.toimage(numpy.array([tuple(pixel) for pixel in row for row in image]))
	generatedImage.show()




generate_maze(10,10)


