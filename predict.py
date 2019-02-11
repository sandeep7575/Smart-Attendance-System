# import the required libraries.
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
from PIL import Image
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/pi/Downloads/Door-unlock-through-face-recongition-\
                master/trainer/trainer.yml')
cascadePath = "/home/pi/Downloads/Door-unlock-through-face-recongition-master\
/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

# UserId and names.
User_ids = 0
person = ['None','Sandeep'] 

# Initialise the camera.
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(1920, 1080))
minW = 0.1*1920
minH = 0.1*1080
 
# Wakeup camera.
time.sleep(0.1)
 
# Capture frames.
for frame in camera.capture_continuous(rawCapture, format="bgr", 
                                       use_video_port=True):
	img = frame.array
	img = cv2.flip(img, -1)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale( 
		gray,
		scaleFactor = 1.2,
		minNeighbors = 5,
		minSize = (int(minW), int(minH)),
	   )
	   
	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
		User_ids, confidence = recognizer.predict(gray[y:y+h,x:x+w])
		confidence = 100 - confidence
		if (confidence > 50):
			User_ids = person[User_ids]
			confidence = "  {0}%".format(round(confidence))
		else:
			User_ids = "unknown"
			confidence = "  {0}%".format(round(confidence))
		
		cv2.putText(img, str(User_ids), (x+5,y-5), font, 1, 
              (255,255,255), 2)
		cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, 
              (255,255,0), 1)  

	cv2.imshow('camera',img)
	key = cv2.waitKey(1) & 0xFF

	rawCapture.truncate(0)

	if key == ord("q"):
		break
		

