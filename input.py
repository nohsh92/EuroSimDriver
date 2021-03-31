import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D

def process_img(original_image):
	processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
	processed_img = cv2.Canny(processed_img, threshold1=50, threshold2=100)
	return processed_img

	
def main():
	for i in list(range(4))[::-1]:
		print(i+1)
		time.sleep(1)

	last_time = time.time()
	while(True):
		# 800x600 windowed mode
		screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
		new_screen = process_img(screen)
		
		print('Pressing W')
		PressKey(W) 
		time.sleep(3)
		print('Releasing W')
		ReleaseKey(W) 

		print('loop took {} seconds'.format(time.time()-last_time))
		last_time = time.time()
		cv2.imshow('window', new_screen)

		#cv2.imshow('window2',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break
			
main()