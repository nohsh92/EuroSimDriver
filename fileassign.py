import numpy as np
import os

def file_number_assignment():
	data_file_no = 0
	
	while True:
		file_name = 'training_data_%d.npy' % (data_file_no)
		
		if os.path.isfile(file_name):
			data_file_no+=1
			print('File exists, moving on to %d th file!'% (data_file_no))
			# training_data = list(np.load(file_name))
		else:
			#print('File does not exist, starting fresh!')
			print('Starting Fresh File Name: %s'%file_name)
			training_data = []
			return file_name, training_data