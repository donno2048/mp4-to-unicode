from PyInstaller.__main__ import run
from shutil import rmtree
from os import unlink
run(['main.py', '-y', '-F', '--console', '-i=logo.ico', '--add-data=video.mp4;.', '-n=main.exe'])
rmtree('build')
unlink('main.exe.spec')
