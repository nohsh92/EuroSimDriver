import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D

def roi(img, vertices):
	mask = np.zeros_like(img)
	cv2.fillPoly(mask, vertices, 255)
	masked = cv2.bitwise_and(img, mask)
	return masked

def process_img(original_image):
	processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
	processed_img = cv2.Canny(processed_img, threshold1=50, threshold2=100) #JC2, 50, 100
	vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500]])
	processed_img = roi(processed_img, [vertices])
	return processed_img

	
def main():

	last_time = time.time()
	while(True):
		# 800x600 windowed mode
		screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
		new_screen = process_img(screen)
		

		print('loop took {} seconds'.format(time.time()-last_time))
		last_time = time.time()
		cv2.imshow('window', new_screen)

		#cv2.imshow('window2',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break
			
main()