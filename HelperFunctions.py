import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import argparse

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
    
def convert_to_number(row,col,width):
    return row*width+col

#converts num back to row, col
def convert_to_index(num,length,width):
    row=int(num/length)
    col=num%width
    return row,col