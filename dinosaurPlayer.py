import pyautogui
import time
import colorsys
import mss
import mss.tools
from PIL import Image
import numpy as np

#pixel to look at for jumps
#530, 325
#height: 20
#width: 20
#find average pixel value for that area

#pixel to look at for ducking
#520, 315
#height: -20
#width: 20
#find average pixel value for that area

print('press crtl+c to quit')
pyautogui.FAILSAFE = True
#this allows you to quit out of the program by moving the mouse to the top left

def lookjump(img):
	shouldjump = False
	for i in range(5):
		pixcolor = img.getpixel((530+i, 345))
		pixcolor = colorsys.rgb_to_hsv(pixcolor[0], pixcolor[1], pixcolor[2])
		if(pixcolor[2] <= 100):
			shouldjump = True
	#print(pixcolor)
	print('pixel value: ' + str(pixcolor[2]))
	if(shouldjump == True):
		pyautogui.press('up')
		print('obstacle detected, jumping...')
		return True
	else:
		print('nothing found, not jumping')

def lookduck(img):
	pixcolor = img.getpixel((520, 315))
	pixcolor = colorsys.rgb_to_hsv(pixcolor[0], pixcolor[1], pixcolor[2])
	#print(pixcolor)
	print('pixel value: ' + str(pixcolor[2]))
	if(pixcolor[2] <= 100):
		pyautogui.press('down')
		print('obstacle detected, ducking')
		#doesn't need to return anything because this is in the else statement of the if loop
	else:
		print('nothing found, not ducking')

try:
	print('3 second countdown now beginning')
	print('3...')
	#gives three second countdown
	time.sleep(1)
	print('2...')
	time.sleep(1)
	print('1...')
	time.sleep(1)
	print('go!')

	#loop begins here
	with mss.mss() as sct:
		while True:
			screenshot = sct.grab(sct.monitors[1])
			img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
			if(lookjump(img) == False):
				lookduck(img)

except KeyboardInterrupt:
    print('\nDone!')
