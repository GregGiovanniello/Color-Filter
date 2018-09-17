"""
program: grayscale.py
author: greg

coverets a photo to greyscale.
"""

from images import Image


def sepia(image):
	grayscale(image)
	for y in range(image.getHeight()):
		for x in range(image.getWidth()):
			(red, green, blue) = image.getPixel(x, y)
			if red < 63:
				red = int(red*1.1)
				blue = int(blue * 0.9)
			elif red < 192:
				red = int(red * 1.15)
				blue = int(blue * 0.85)
			else: 
				red = min(int(red* 1.08), 255)
				blue = int(blue * 0.93)
			image.setPixel(x, y,(red, green, blue))
				
def grayscale(image):
	# converts image to grayscale
	for y in range(image.getHeight()):
		for x in range(image.getWidth()):
			(red, green, blue) = image.getPixel(x, y) 
			red = int(red * 0.299)
			green = int(green * 0.587)
			blue = int(blue * 0.114)
			lum = red + green + blue
			image.setPixel(x, y, (lum, lum, lum))
			
def main():
	filename = input("Type the image you would like to use ")
	image = Image(filename)
	grayscale(image)
	print("Close the image window to continue. ")
	image.draw()
	sepia(image)
	print("Close the image window to quit. ")
	image.draw()
	
if __name__ == "__main__":
	main()