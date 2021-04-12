try: from PIL.Image import open
except: from Image import open
from sys import stdout, argv
from cv2 import VideoCapture, imwrite, resize
th = 127
def I2T(File):
	im = open(File)
	(w, h) = im.size
	mim = im.convert("1")
	data = list(mim.getdata())
	counter = 0
	field = True
	for pixel in data:
		if field:
			if pixel > th: stdout.write("*")
			else: stdout.write(" ")
		counter = counter + 1
		if counter >= w:
			counter = 0
			if field: stdout.write("\n")
			field = not field
vidcap = VideoCapture(argv[1])
success, image = vidcap.read()
while success:
	imwrite(".jpg", resize(image, (144, 108), interpolation = 3))
	I2T(".jpg")
	success, image = vidcap.read()
	print("R")
