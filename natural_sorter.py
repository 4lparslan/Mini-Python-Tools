# The code sorts elements of the list. (Natural sort)

import os
import natsort

path = r'/my/path/'

all_images = []

for filename in os.listdir(path):
    all_images.append(filename)  

sorted_list = natsort.natsorted(all_images)