from curses import wrapper
try: from PIL.Image import open
except ImportError: from Image import open
from cv2 import VideoCapture, imencode, resize
from io import BytesIO
from ctypes import WinDLL
def play(window):
	try: from sys import _MEIPASS
	except ImportError::
		from os.path import abspath
		_MEIPASS = abspath(".")
	vidcap = VideoCapture(_MEIPASS + "/video.mp4")
	success, image = vidcap.read()
	while success:
		for l in I2T(BytesIO(imencode(".jpg", resize(image, (144, 108), interpolation = 3))[1])).split("\n"):
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
WinDLL('user32').ShowWindow(WinDLL('user32').GetForegroundWindow(), 3)
wrapper(play)
