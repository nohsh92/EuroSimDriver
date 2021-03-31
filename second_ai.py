#second_ai.py

import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from numpy import ones,vstack
from numpy.linalg import lstsq
from directkeys import PressKey, ReleaseKey, W, A, S, D
from statistics import mean
from draw_lanes import draw_lanes
from grabscreen import grab_screen



def roi(img, vertices):

    #blank mask:
    mask = np.zeros_like(img)   
    
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, vertices, 255)
    
    #returning the image only where mask pixels are nonzero
    masked = cv2.bitwise_and(img, mask)
    return masked




def process_img(image):
	original_image = image
	# convert to gray
	processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# edge detection
	processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=400)

	processed_img = cv2.GaussianBlur(processed_img,(5,5),0)

	vertices = np.array([[10,760],[10,500],[300,350],[700,350],[1015,550],[1015,760],[745,760],[530,475],[345,760]])

	processed_img = roi(processed_img, [vertices])

	# more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
	#                                     rho   theta   thresh  min length, max gap:      	
	lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 80, 200, 5) #180 20 
	m1 = 0
	m2 = 0
	try:
		l1, l2, m1, m2 = draw_lanes(original_image,lines)
		cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [0,255,0], 30)
		cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0,255,0], 30)
	except Exception as e:
		print(str(e))
		pass
	try:
		for coords in lines:
			coords = coords[0]
			try:
				cv2.line(processed_img, (coords[0], coords[1]), (coords[2], coords[3]), [255,0,0], 3)
				
				
			except Exception as e:
				print(str(e))
	except Exception as e:
		pass

	return processed_img,original_image, m1, m2

	
# def straight():
	# PressKey(W)
	# ReleaseKey(A)
	# ReleaseKey(D)
	# time.sleep(0.2)
	# ReleaseKey(W)

# def left():
	# PressKey(A)
	# PressKey(W)
	# time.sleep(0.2)
	# ReleaseKey(W)
	# ReleaseKey(D)
	# ReleaseKey(A)

# def right():
	# PressKey(D)
	# PressKey(W)
	# time.sleep(0.2)
	# ReleaseKey(A)
	# ReleaseKey(W)
	# ReleaseKey(D)

# def slow():
	# ReleaseKey(W)
	# ReleaseKey(A)
	# ReleaseKey(D)

	
def main():
	for i in list(range(5))[::-1]:
		print(i+1)
		time.sleep(1)
		
	last_time = time.time()
	while True:
		screen =  grab_screen(region=(0,40,1024,768))
		print('Frame took {} seconds'.format(time.time()-last_time))
		last_time = time.time()
		new_screen,original_image, m1, m2 = process_img(screen)
		#cv2.imshow('window', new_screen)
		cv2.imshow('window2',cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))

		if m1 < 0 and m2 < 0:
			# right()
			print("RIGHT")
		elif m1 > 0 and m2 > 0:
			# left()
			print("LEFT")
		else:
			# straight()
			print("STRAIGHT")

		#cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break
			
			
main()

