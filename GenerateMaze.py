import random
import numpy
import scipy.misc as smp
'''
Purpose: Functions to generate maze using various different methods
'''

def generate_maze_DFS(length,width):
	#dimensions:length, width
	#generates maze using randomized depth first search walks

	#create matrix and fill with ones
	#represents actual maze, where 1's are walls and 0's are traversable territory



	maze=[[1]*width for i in range(length)]
	#always start at 0,0
	row=0
	col=0
	stack=[]#stores locations we have visited but not backtracked to
	stack.append([0,0])
	moves={
	'up':[-1,0],
	'down':[1,0],
	'left':[0,-1],
	'right':[0,1]
	}
	while(stack):
		maze[row][col]=0#visited
		validMoves=[]
		#if moving up is still on maze, and that location has not yet been visited
		if(row-1>0 and maze[row-1][col]==1):
			validMoves.append('up')
		if(col-1>0 and maze[row][col-1]==1):
			validMoves.append('left')
		if(row+1<length-1 and maze[row+1][col]==1):
			validMoves.append('down')
		if(col+1<width-1 and maze[row][col+1]==1):
			validMoves.append('right')

		#if there are valid moves form 
		if len(validMoves):
			nextMove=moves[random.choice(validMoves)]
			stack.append([row,col])#to facilitate backtracking, add to list
			row+=nextMove[0]
			col+=nextMove[1]
		else:
			row,col=stack.pop()
	return maze

for row in generate_maze_DFS(10,10):
	print(row)




def generate_maze_DFS_old(length, width):
	#dimensions:length, width
	#generates maze using randomized depth first search walks
	#create matrix and fill with ones
	#represents actual maze, where 1's are walls and 0's are traversable territory
	maze=[[1]*width for i in range(length)]
	visited=[]#stores cells that have already been visited
	stack=[]#stack to facilitate random walk across matrix
	currentLength=random.randint(0,length-1)#for simplicity: always start at left side of maze
	currentWidth=0#always starting on left side of maze
	stack.append([currentLength,currentWidth])#push starting index onto stack
	visited.append([currentLength,currentWidth])
	#continue walk while there are still unvisited non-dead-ends
	while(stack):
		current=stack.pop()#retrieve latest length and width
		maze[current[0]][current[1]]=0#now that walls has been visited, add it to valid maze path
		#if 1: choose top(length-1)
		#if 2: choose bottom(length+1)
		#if 3: choose left(width-1)
		#if 4: choose right(width+1)
		allowedVals=[1,2,3,4]
		transform=random.choice(allowedVals)
		choiceRow,choiceCol=get_next_dimensions(current,transform)
		allowedVals.remove(transform)#make sure we don't select same index again
		#loop through all choices in random order until next item is found or everything is determined...
		#to be dead ends
		iteration=0#four possibilities for next location:up down, right,left
		while(iteration<4):
			#check if choiceRow and choiceCol correspond to dead end
			#if they do: 
			#     choose next transform, remove from allowedVals, call get_next_dimensions(current,transform)
			#if not, set foundNext=True, add [choiceRow,choiceCol] to stack
			#first make sure that choiceRow and choiceCol are within dimension limits
			if [choiceRow,choiceCol] not in visited and choiceRow in range(0,length) and choiceCol in range(0,width):
				parameters={
				'maze':maze,
				'visited':visited,
				'prev':[current[0],current[1]],
				'rowCheck':choiceRow,
				'colCheck':choiceCol
				}
				#we have found valid index
				if(not is_dead_end(parameters)):
					stack.append([choiceRow,choiceCol])
					visited.append([choiceRow,choiceCol])
			if allowedVals:
				transform=random.choice(allowedVals)
				choiceRow,choiceCol=get_next_dimensions(current,transform)
				allowedVals.remove(transform)#make sure we don't select same index again
			iteration+=1
	print(maze)
	return maze

	
def get_next_dimensions(dimensions,transformationNumber):
	#given: dimensions set and number corresponding to specific transformation
	#dimensions given in form: [length,width]
	#transformationNumber given as number 1-4
	#if 1: choose top(length-1)
	#if 2: choose bottom(length+1)
	#if 3: choose left(width-1)
	#if 4: choose right(width+1)
	#return dimensions with transformation applied
	returnLength=dimensions[0]+(0 if transformationNumber in (3,4) else -1 if transformationNumber==1 else 1)
	returnWidth=dimensions[1]+(0 if transformationNumber in (1,2) else -1 if transformationNumber==3 else 1)
	return [returnLength,returnWidth]



def is_dead_end(parameters):
	#given: maze matrix, list of visited indexes, row/column to check, row/column of previous index
	#check all neighboring indexes that are not previous
	#if an index is found that is visited, return True (dead end)
	#else, return False (not dead end)
	maze=parameters['maze']
	visited=parameters['visited']
	rowCheck=parameters['rowCheck']#row of space to check
	colCheck=parameters['colCheck']#col of space to check
	prev=parameters['prev']
	#is dead end if all neighboring cells have been visited
	#return False if any neighboring cell has not been visited
	if(not (prev==[rowCheck+1,colCheck]) and [rowCheck+1,colCheck] in visited):
		return True
	if(not (prev==[rowCheck-1,colCheck]) and [rowCheck-1,colCheck] in visited):
		return True
	if(not (prev==[rowCheck,colCheck+1]) and [rowCheck,colCheck+1] in visited):
		return True
	if(not (prev==[rowCheck,colCheck-1]) and [rowCheck,colCheck-1] in visited):
		return True
	return False


def generate_image(maze):
	#given maze data(1 represents edges, 0 represents path)
	#create image representing maze
	imageArr=[]#stores completed rgb array
	index=0
	for row in maze:
		imageArr.append([])
		for pixel in row:
			if pixel==1:
				imageArr[index].append((0,0,0))
			elif pixel==0:
				imageArr[index].append((255,255,255))
		index+=1
	imagePixels=numpy.array(imageArr)
	image=smp.toimage(imagePixels)
	image.show()






	
