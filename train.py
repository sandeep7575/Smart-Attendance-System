# Import the required libraries.
import cv2
import numpy as np
from PIL import Image
import os


# Location where pics saved.
img_path = '/home/pi/Downloads/Door-unlock-through-face-recongition-\
master/dataset'

# Identify face.
recognizer = cv2.face.LBPHFaceRecognizer_create()

identifier = cv2.CascadeClassifier("/home/pi/Downloads/Door-unlock-through-\
                                   face-recongition-master/haarcascade_\
                                   frontalface_default.xml");

# Detect face.
def face_detect(img_path):
    locs = [os.path.join(img_path,f) for f in os.listdir(img_path)]     
    Samples=[]
    User_ids = []

    for loc in locs:

        PIL_img = Image.open(loc).convert('L')
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(loc)[-1].split(".")[1])
        faces = identifier.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            Samples.append(img_numpy[y:y+h,x:x+w])
            User_ids.append(id)

    return Samples,User_ids

print ("\n Training User faces. Please Wait ...")
faces,User_ids = face_detect(img_path)
recognizer.train(faces, np.array(User_ids))

# Save the model into trainer/trainer.yml
recognizer.write('/home/pi/Downloads/Door-unlock-through-face-recongition-\
                 master/trainer/trainer.yml') 

# Number of user face id trained.
print("\n {0} faces trained.".format(len(np.unique(User_ids))))
