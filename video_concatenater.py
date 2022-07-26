# The code bring two videos together. So you can compare similar videos on one screen.

import cv2
import numpy as np

cap1 = cv2.VideoCapture('/my/path/my_video.mp4')
cap2 = cv2.VideoCapture('/my/other/path/my_other_video.mp4')

# Set output video resolution:
# For hstack (2*width , height)
# For vstack (width , 2*height)
out = cv2.VideoWriter('/my/new/path/my_new_video.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 20, (3840,1080)) # change '20' value as your video's FPS

size = cap1.get(cv2.CAP_PROP_FRAME_COUNT)
counter = 0

while True:
  # Capture frame-by-frame
	ret1, frame1 = cap1.read()
	ret2, frame2 = cap2.read()

	if ret1 == False or ret2 == False:
		break

	if (ret1 == True) and (ret2 == True):
		new_frame = np.hstack((frame1,frame2)) # hstack for horizontal concetanation. Use vstack for vertical concetanation.
		out.write(new_frame)

	print(str(counter) + "/" + str(size))
	counter+=1


# When everything done, release the video capture object
cap1.release()
cap2.release()
out.release()
# Closes all the frames
cv2.destroyAllWindows()