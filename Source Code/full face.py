import numpy as np
import cv2
import subprocess as sp

cap = cv2.VideoCapture(0)

while(True):
    
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
##    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_cascade1 = cv2.CascadeClassifier('right eye.xml')
    face_cascade2 = cv2.CascadeClassifier('left eye.xml')
    face_cascade3 = cv2.CascadeClassifier('Mouth.xml')
    face_cascade4 = cv2.CascadeClassifier('nose.xml')

    eyes_r = face_cascade1.detectMultiScale(frame, 1.2, 8)
    eyes_l = face_cascade2.detectMultiScale(frame, 1.5, 13)
    Mouths = face_cascade3.detectMultiScale(frame, 1.5, 13)
    noses = face_cascade4.detectMultiScale(frame, 1.9, 10)

    tmp = sp.call('cls',shell=True)
    print("Found " +str(len(eyes_r))+ " right eye(s)")
    print("Found " +str(len(eyes_l))+ " left eye(s)")
    print("Found " +str(len(Mouths))+ " Mouth(s)")
    print("Found " +str(len(noses))+ " nose(s)")
    
    for (x,y,w,h) in eyes_r:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    for (x,y,w,h) in eyes_l:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

    for (x,y,w,h) in Mouths:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    for (x,y,w,h) in noses:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
