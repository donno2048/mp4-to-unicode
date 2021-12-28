# mp4-to-unicode

Use this to show a video in the terminal (Unicode art)

## Usage

Run `python3 main.py <video.mp4>` with the terminal **maximized** to display _<video.mp4>_ as ascii art.

If you get `_curses.error: addwstr() returned ERR` try decreasing the font size.

## Install dependencies

`pip3 install opencv-python Pillow`

(on Linux you may need to run `sudo apt-get install ffmpeg libsm6 libxext6 -y` to use `opencv`)

<br/>

I usually don't create a PyPi package **and** a "usual program" but this is a special case, you can view the [pypi package](https://github.com/donno2048/mp42uni) (it's actually better)
