#live face and eye detection slash tracking
# https://opencv-python-tutorials.readthedocs.io/zh/latest/10.%20%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B/10.1.%20%E9%87%87%E7%94%A8Haar%20Cascades%E8%BF%9B%E8%A1%8C%E4%BA%BA%E8%84%B8%E6%A3%80%E6%B5%8B/
# haar cascade explanation  : pre-trained classifier
import cv2
import numpy as np

cap = cv2.VideoCapture("tutorial\TobocanAvecLesGrandsParents.mp4")
#loading the classifier
face_cascade =cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')#argument: path
eye_cascade =cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')#argument: path
#use it



while True:
    ret, frame = cap.read()
#pass le frame en gray scale puis le passer à face_cascade, le face_cascade nous rend tous les locations de face
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)#https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters
    for(x, y , w, h) in faces:#c'est un rectangle, 
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)
        #confirme c'est un visage dans ce rectangle par les yeux
        roi_gray = gray[ y:y+h,x:x+w]#d'abord ligne ensuiste column
        roi_color = frame[ y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3,5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0),5)
    if ret == True:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
