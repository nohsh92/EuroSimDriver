# train_model.py

import numpy as np
from alexnet import alexnet

WIDTH = 205		# 80
HEIGHT = 155	# 60
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'pyET2-car-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2', EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

print('Ready to load data, loading now: ')
train_data = np.load('shuffled_final.npy')

print('Done loading')
train = train_data[:-500]
test = train_data[-500:]

X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
test_y = [i[1] for i in train]

model.fit({'input':X}, {'targets':Y}, n_epoch=EPOCHS,
	validation_set=({'input':test_x}, {'targets':test_y}),
	snapshot_step=500, show_metric=True, run_id=MODEL_NAME)
	
# tensorboard --logdir=foo:C:\PythonET2\snoh_ET_v3_training_alexnet\log

model.save(MODEL_NAME)