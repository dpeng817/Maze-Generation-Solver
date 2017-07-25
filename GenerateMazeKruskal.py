import random
import unionfind
import argparse
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import HelperFunctions as hf

#given length and width, generate maze using kruskal's minimum spanning tree algorithm



def generate_maze(length,width):
    #generate edges
    edges=hf.generate_edges(length,width)
    #generate maze
    maze=hf.generate_blank_maze(length,width)
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
        end=hf.convert_to_number(endRow,endCol,width)
        #get unique number identifier for prevRow,prevCol
        prev=hf.convert_to_number(prevRow,prevCol,width)
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
    hf.generate_image(maze,length,width)



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
