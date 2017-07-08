from PIL import Image
import random
'''
Purpose: Functions to generate maze using various different methods
'''

def generate_maze_DFS(length, width):
	#dimensions:length, width
	#generates maze using randomized depth first search walks

	#create matrix and fill with ones
	#represents actual maze, where 1's are walls and 0's are traversable territory
	walls=[[1]*width]*length
	visited=[]#stores cells that have already been visited
	stack=[]#stack to facilitate random walk across matrix
	currentLength=random.randint(0,length)#for simplicity: always start at left side of maze
	currentWidth=0#always starting on left side of maze
	stack.append([currentLength,currentWidth])#push starting index onto stack
	#continue walk while there are still unvisited non-dead-ends
	while(stack):
		current=stack.pop()#retrieve latest length and width
		#if 1: choose top(length-1)
		#if 2: choose bottom(length+1)
		#if 3: choose left(width-1)
		#if 4: choose right(width+1)
		foundNext=False#false if nothing has been yet added to stack, true if it has
		allowedVals=[1,2,3,4]
		transform=random.choice(allowedVals)
		choiceRow,choiceCol=get_next_dimensions(current,transform)
		allowedVals.remove(transform)#make sure we don't select same index again
		#loop through all choices in random order until next item is found or everything is determined...
		#to be dead ends
		while(allowedVals and not foundNext):
			#check if choiceRow and choiceCol correspond to dead end
			#if they do: 
			#     choose next transform, remove from allowedVals, call get_next_dimensions(current,transform)
			#if not, set foundNext=True, add [choiceRow,choiceCol] to stack


	
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


	
