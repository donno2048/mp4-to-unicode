from curses import error, wrapper
from time import sleep
from subprocess import Popen
from os import system
from sys import argv
def play(window):
	for l in open(__file__.replace("py", "txt")):
		# sleep(x) # Use this to change the fps
		if l[0] == 'R': window.move(0,0)
		else:
			window.addstr(l)
			window.refresh()
i = input("Would you like to use vlc to see the original video with sound in the meanwhile? (y\\n)\nIf you do please install it (sudo apt-get install vlc -y)\n").lower()
while True:
	if i in ["y", "n"]: break
	i = input("Please write either \"y\" or \"n\" ")
system(f"python3 {__file__.replace('main', 'process')} {argv[1]} > {__file__.replace('py', 'txt')}")
if i == "y": pid = Popen(["cvlc", "video.mp4"], stdout=-1, stderr=-1)
sleep(2)
try: wrapper(play)
except Exception as e:
	if i== "y": pid.terminate()
	print(e)
