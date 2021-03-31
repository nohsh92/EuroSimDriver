# test_model.py

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
from alexnet import alexnet
import os
from fileassign import file_number_assignment
from directkeys import PressKey, ReleaseKey, W, A, S, D

WIDTH = 205		# 80
HEIGHT = 155	# 60
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'pyET2-car-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2', EPOCHS)

def straight():
	PressKey(W)
	ReleaseKey(A)
	ReleaseKey(D)
	time.sleep(0.2)
	ReleaseKey(W)

def left():
	PressKey(A)
	PressKey(W)
	time.sleep(0.2)
	ReleaseKey(W)
	ReleaseKey(D)
	ReleaseKey(A)

def right():
	PressKey(D)
	PressKey(W)
	time.sleep(0.2)
	ReleaseKey(A)
	ReleaseKey(W)
	ReleaseKey(D)
	
model = alexnet (WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def main():

	for i in list(range(4))[::-1]:
		print(i+1)
		time.sleep(1)

	paused = False
	
	last_time = time.time()
	
	while(True):
		
		if not paused:
			# 800x600 windowed mode  ==> changed for EuroTruck
			screen = grab_screen(region=(0,40,1024,768))
			screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
			screen = cv2.resize(screen, (205,155))

			print('Frame took {} seconds'.format(time.time()-last_time))
			last_time = time.time()
			
			prediction = model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
			moves = list(np.around(prediction))
			print(moves, prediction)
			
			if moves == [1,0,0]:
				left()
			elif moves == [0,1,0]:
				straight()
			elif moves == [0,0,1]:
				right()

		keys = key_check()
		if 'I' in keys:
			if paused:
				paused = False
				print('unpaused!')
				time.sleep(1)
			else:
				print('Pausing!')
				paused = True
				ReleaseKey(A)
				ReleaseKey(W)
				ReleaseKey(D)
				time.sleep(1)


main()
