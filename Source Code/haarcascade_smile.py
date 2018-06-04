import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
##    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
    face_cascade2 = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    faces = face_cascade2.detectMultiScale(frame, 1.2, 5)
    smiles = face_cascade.detectMultiScale(frame, 1.1, 3)
##    print("Found " +str(len(smiles))+ " smiling face(s)")
    for (x,y,w,h) in faces:
        for (x1,y1,w1,h1) in smiles:
            if ((x1 > x) and (y1>y)) and ((x1 < w) and (y1< h)):
                cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
