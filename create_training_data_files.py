# create_training_data.py

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os
from fileassign import file_number_assignment


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array

    [A,W,D] boolean values.
    '''
    output = [0,0,0]
    
    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output




def main():
	temp_file_name, temp_training_data = file_number_assignment()

	for i in list(range(4))[::-1]:
		print(i+1)
		time.sleep(1)


	paused = False
	while(True):

		if not paused:
			# 800x600 windowed mode  ==> changed for EuroTruck
			screen = grab_screen(region=(0,40,1024,768))
			last_time = time.time()
			screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
			screen = cv2.resize(screen, (205,155))
			#screen = cv2.resize(screen, (160,120))
			# resize to something a bit more acceptable for a CNN
			keys = key_check()
			output = keys_to_output(keys)
			temp_training_data.append([screen,output])

			if len(temp_training_data) % 100 == 0:
				print(len(temp_training_data))
			if len(temp_training_data) % 1000 == 0:
				print(len(temp_training_data))
				np.save(temp_file_name,temp_training_data)
				
				temp_file_name, temp_training_data = file_number_assignment()

		keys = key_check()
		if 'T' in keys:
			if paused:
				paused = False
				print('unpaused!')
				time.sleep(1)
			else:
				print('Pausing!')
				paused = True
				time.sleep(1)


main()
