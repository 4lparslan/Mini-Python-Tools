# The code generates validation.txt and train.txt files. Seperation of images is done randomly. You can specify val-train ratio.
# So you can generate validation and train datasets for training an Artificial Neural Network
import os
import cv2
import random

# Specify validation dataset ratio. %20 val %80 train recommended.
VAL_RATIO = 20

path = r'/my/dataset'

train = open('train.txt','w')
val = open('valid.txt','w')

all_images = []

for filename in os.listdir(path):
    if filename.endswith(".jpg"):
       # name= filename.split('.jpg')
        fullname = os.path.join(path, filename)
        all_images.append(fullname)
        
random.shuffle(all_images)

length = len(all_images)
val_size = int(length * VAL_RATIO / 100)
train_size = length - val_size

for i in range(val_size):
    val.write(all_images[i])
    val.write('\n')

for j in range(train_size):
    train.write(all_images[j+val_size])
    train.write('\n')
    
train.close()
val.close()