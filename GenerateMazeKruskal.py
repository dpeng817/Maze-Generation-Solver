import random
import unionfind
import argparse
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

#given length and width, generate maze using kruskal's minimum spanning tree algorithm

def generate_edges(length,width):
    #endlocation: location that direction moves to
    #direction: direction taken to get to endlocation
    result=[]
    for row in range(0,length):
        for col in range(0,width):
            #left
            if col>0:
                result.append({
                    'endLocation':(row,col),
                    'direction':'left'
                    })
            #right
            if col<width-1:
                result.append({
                    'endLocation':(row,col),
                    'direction':'right'
                    })
            #up
            if row>0:
                result.append({
                    'endLocation':(row,col),
                    'direction':'up'
                    })
            #down
            if row<length-1:
                result.append({
                    'endLocation':(row,col),
                    'direction':'down'
                    })
    return result

def generate_maze(length,width):
    #generate edges
    edges=generate_edges(length,width)
    #generate maze
    maze=generate_blank_maze(length,width)
    sets=unionfind.unionfind(len(edges))
    #shuffle edges
    random.shuffle(edges)
    while(edges):
        currentEdge=edges[-1]#get last element in list
        endRow,endCol=currentEdge['endLocation']
        direction=currentEdge['direction']
        prevRow,prevCol={
                'left':(endRow,endCol-1),
                'right':(endRow,endCol+1),
                'up':(endRow-1,endCol),
                'down':(endRow+1,endCol)
                }[direction]
        #get unique number identifier for endRow,endCol
        end=convert_to_number(endRow,endCol,width)
        #get unique number identifier for prevRow,prevCol
        prev=convert_to_number(prevRow,prevCol,width)
        #if end and prev are not in same set, then remove wall between them and join set
        if not sets.issame(end,prev):
            #if direction is right
            #set prevlocation right to 1,endlocation left to 1
            if direction=='right':
                maze[endRow][endCol]['right']=1
                maze[prevRow][prevCol]['left']=1
            if direction=='left':
                maze[endRow][endCol]['left']=1
                maze[prevRow][prevCol]['right']=1
            if direction=='up':
                maze[endRow][endCol]['up']=1
                maze[prevRow][prevCol]['down']=1
            if direction=='down':
                maze[endRow][endCol]['down']=1
                maze[prevRow][prevCol]['up']=1
            sets.unite(prev,end)
        #if in same set, remove edge from list
        else:
            edges.pop()
    maze[0][0]['up']=1
    maze[length-1][width-1]['right']=1
    generate_image(maze,length,width)


#converts row,col to number from row and col
def convert_to_number(row,col,width):
    return row*width+col

#converts num back to row, col
def convert_to_index(num,length,width):
    row=int(num/length)
    col=num%width
    return row,col

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
