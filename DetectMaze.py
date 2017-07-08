from PIL import Image

'''
Purpose: 
Given RGB image, convert to grayscale, then read it in as a matrix of 1's and 0's
'''

def representation(filePath):
	'''
	takes an image of maze and converts it to array of 1's and 0's
	'''
	imageFile=Image.open(filePath)#open image
	imageFile=imageFile.convert('1')#convert image to grayscale
	pixels=list(imageFile.getdata())#iterable list of pixels in image
	width,height=imageFile.size#get height and width of image(in pixels)
	pixels=[pixels[i * width:(i + 1) * width] for i in range(height)]#converts image into iterable matrix
	return [[1 if pixel==255 else 0 for pixel in row] for row in pixels]#takes values of 255, converts to 0, 



