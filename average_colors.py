
from PIL import Image
import cv2
""" Returns a 3-tuple containing the RGB value of the average color of the
given square bounded area of length = n whose origin (top left corner) 
is (x, y) in the given image"""
filename = 'meow.jpg'
image2 = cv2.imread(filename) 
def get_average_color(x,y, n, imagePath):
	image = Image.open(imagePath).load()
	r, g, b = 0, 0, 0
	count = 0
	for s in range(x, x+n+1):
		for t in range(y, y+n+1):
			pixlr, pixlg, pixlb = image[s, t]
			r += pixlr
			g += pixlg
			b += pixlb
			count += 1
	cv2.rectangle(image2, (x, y), (x + n, y + n), ((b/count), (g/count), (r/count)), -1)
	return ((r/count), (g/count), (b/count))

r, g, b = get_average_color(240,500, 50, filename)
r, g, b = get_average_color(140,480, 50, filename)
r, g, b = get_average_color(340,190, 50, filename)
r, g, b = get_average_color(250,350, 50, filename)
r, g, b = get_average_color(400,270, 50, filename)
r, g, b = get_average_color(390,500, 50, filename)
r, g, b = get_average_color(400,390, 50, filename)
cv2.imwrite("./meow2.jpg",image2)
print(r,g,b)