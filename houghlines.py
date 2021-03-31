import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D

def draw_lines(img, lines):
	try:
		for line in lines:
			coords = line[0]
			cv2.line(img, (coords[0],coords[1]) , (coords[2],coords[3]), [255,255,255], 5)
	except:
		pass
		
def roi(img, vertices):
	mask = np.zeros_like(img)
	cv2.fillPoly(mask, vertices, 255)
	masked = cv2.bitwise_and(img, mask)
	return masked

def process_img(original_image):
	processed_img = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
	processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=400) #JC2, 50, 100
	cv2.imshow('window2_canny', processed_img)

	
	processed_img = cv2.GaussianBlur(processed_img, (5,5), 0)
	cv2.imshow('window3_gau', processed_img)
	
	vertices = np.array([[10,760],[10,500],[300,350],[700,350],[1015,550],[1015,760],[745,760],[530,475],[345,760]])
	processed_img = roi(processed_img, [vertices])
	cv2.imshow('window4_roi', processed_img)
		
	#						edges
	lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 80, 200, 5) #180 20 15
	draw_lines(processed_img, lines)
	
	return processed_img

	
def main():

	last_time = time.time()
	while(True):
		# 800x600 windowed mode
		screen =  np.array(ImageGrab.grab(bbox=(0,40,1024,768)))
		new_screen = process_img(screen)
		

		print('loop took {} seconds'.format(time.time()-last_time))
		last_time = time.time()
		cv2.imshow('window', new_screen)

		#cv2.imshow('window2',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break
			
main()