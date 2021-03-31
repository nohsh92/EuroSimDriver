#balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import os


# data_file_number = 0
# ../ET_data_files/v1_WAD_overall
# data_file_name = 'training_data_%d.npy' % (data_file_number)

data_file_name = '../ET_data_files/v1_WAD_overall/overall_save_data.npy' # % (data_file_number)
overall_training_data = []

lefts = []
rights = []
forwards = []

print('loading:')
train_data = np.load(data_file_name)

print('done loading. processing:')

df1 = pd.DataFrame(train_data)
print(df1.head())
print(Counter(df1[1].apply(str)))

for data in train_data:
	img = data[0]
	choice = data[1]
	
	print(choice)
	
	if choice == [1, 0, 0]:
		lefts.append([img,choice])

	elif choice == [0, 1, 0]:
		rights.append([img,choice])
	
	elif choice == [0, 0, 1]:
		forwards.append([img,choice])
	
	else:
		print('no matches')

		
print('putting it back together')

forwards = forwards[:len(lefts)][:len(rights)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]

final_data = forwards + lefts + rights

print('stats for the final data:')
df2 = pd.DataFrame(final_data)
print(df2.head())
print(Counter(df1[1].apply(str)))

shuffle(final_data)

np.save('shuffled_final.npy', final_data)

print('finished')
		
# df = pd.DataFrame(train_data)
# print(df.head())

# print('applying counter: ')
# print(Counter(df[1].apply(str)))
