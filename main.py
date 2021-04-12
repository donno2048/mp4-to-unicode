from curses import wrapper
from time import sleep
from subprocess import Popen
from sys import argv
try: from PIL.Image import open
except: from Image import open
from cv2 import VideoCapture, imwrite, resize
def play(window):
	vidcap = VideoCapture(argv[1])
	success, image = vidcap.read()
	while success:
		imwrite(__file__.replace(".py", ".jpg"), resize(image, (144, 108), interpolation = 3))
		for l in I2T(__file__.replace(".py", ".jpg")).split("\n"):
			# time.sleep(x) # Use this to change the fps
			window.addstr(l + "\n")
			window.refresh()
		window.move(0, 0)
		success, image = vidcap.read()
def I2T(File):
	text, im, counter, field= "", open(File), 0, True
	for pixel in list(im.convert("1").getdata()):
		if field: text += "*" if pixel > 127 else " "
		counter += 1
		if counter >= im.size[0]:
			counter = 0
			if field: text += "\n"
			field = not field
	return text
i = input("Would you like to use vlc to see the original video with sound in the meanwhile? (y\\n)\nIf you do please install it (sudo apt-get install vlc -y)\n").lower()
while True:
	if i in ["y", "n"]: break
	i = input("Please write either \"y\" or \"n\" ")
if i == "y": pid = Popen(["cvlc", argv[1]], stdout=-1, stderr=-1)
sleep(2)
try: wrapper(play)
except Exception as e:
	if i== "y": pid.terminate()
	print(e)
