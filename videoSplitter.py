import cv2
import os

# Add your video file to the same path as the videoSplitter.py file. 
# Be sure that there is only one video file in the path. Or you can manually specify the name of the file below

path = 'C:\\write\\your\\path' # add input path here
extensions = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.webm', 'flv', '.mpeg']
outputFolder = "output" # specify the name of the output folder
fname = "frame" # specify the prename for files
count = 0 # choose index start number
numberOfJump = 10 # If you want fewer frames for each second of the video, enter an integer greater than 0. Or you can delete the for loop in the while loop

files = os.listdir(path)

for index, file in enumerate(files):
    if file.endswith(tuple(extensions)):
        cap = cv2.VideoCapture(file)

# cap = cv2.VideoCapture('example.mp4') #you can manually add you own video file here. First, delete the for loop above
success,image = cap.read()

if not os.path.exists(outputFolder): #check if there is an output folder. If not create it
  os.makedirs(outputFolder)
 
while success:     
  filename = outputFolder + '/' + fname + str(count) + ".jpg" # Remember to specify the extension for images
  cv2.imwrite(filename, image)
  # print('Reading: frame' + str(count) , success)
  for n in range(numberOfJump):  
    success,image = cap.read()
  count += 1