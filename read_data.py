import os
import numpy as np

data_file_number = 0

while True:
	data_file_name = 'training_data_%d.npy' % (data_file_number)
	
	print('%s' % (data_file_name))
	
	if os.path.isfile(data_file_name):
		print('File exists, extracting data: %s' % (data_file_name))
		# data_file_number+=1
		file_data = np.load(data_file_name)
		print(file_data)
		
	else:
		print('Finished!')
		break