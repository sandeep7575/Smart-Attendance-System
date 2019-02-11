# Import all the required libraries.
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
from PIL import Image
import os



# Initializing the camera.
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(1920, 1080))
minW = 0.1*1920
minH = 0.1*1080
 
# Get the harcascade file.
face_identity = cv2.CascadeClassifier('/home/pi/Downloads/Door-unlock-through\
                                      -face-recongition-master/\
                                      haarcascade_frontalface_default.xml')
# Enter user ID to record.
user_id = input('\n Enter Used ID =  ')

 
# Wakeup camera.
time.sleep(0.1)
pics = 0
# Capture the frames from the camera.
for frame in camera.capture_continuous(rawCapture, format="bgr", 
                                       use_video_port=True):
	img = frame.array
	img = cv2.flip(img, -1)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	faces = face_identity.detectMultiScale( 
		gray,
		scaleFactor = 1.2,
		minNeighbors = 5,
		minSize = (int(minW), int(minH)),
	   )
	   
	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)     
		pics += 1
		# Save the captured image into the datasets folder
		cv2.imwrite("/home/pi/Downloads/\
              Door-unlock-through-face-recongition-master/dataset/Face." + 
              str(user_id) + '.' + str(pics) + ".jpg", gray[y:y+h,x:x+w])

	cv2.imshow('camera',img)
	key = cv2.waitKey(1) & 0xFF

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)

	if key == ord("q"):
		break
	#	break
	elif pics >= 50:
		break
		

