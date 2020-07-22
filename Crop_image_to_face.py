import numpy as np
import cv2
import matplotlib.pyplot as plt
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x-15, y-75), (x + w+15, y + h+25), (255, 0, 0), 2)
        X = x
        Y = y
        W = w
        H = h
    cv2.imshow('img', img)
    
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break         
        


roi = img[Y-75:Y+H+25, X-15:X+W+15]
cv2.imwrite("image.jpg", roi)
#cv2.imwrite("filename.jpg",img)
cap.release()