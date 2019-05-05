# -*- coding: utf-8 -*-

import cv2
import face_recognition
import time
import serial

#establish connection with arduino on port COM4
arduino = serial.Serial('COM4', 9600) 
time.sleep(2)
print("Connection to arduino...")

                                  #training
#reading my pic
person1 = face_recognition.load_image_file("C:/Users/Ebtesam/Desktop/Project/person1.jpg")
#encoding face features from my pic.
encoding_person1 = face_recognition.face_encodings(person1)[0]

person2 = face_recognition.load_image_file("C:/Users/Ebtesam/Desktop/Project/person2.jpg")
encoding_person2 = face_recognition.face_encodings(person2)[0]


while(True):
    # Capture frame by frame
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    
    #saving a test frame
    img = "test.png"
    cv2.imwrite(img, frame)
    
    #encode features of test pic.
    picture = face_recognition.load_image_file(img)
    encoding_picture1 = face_recognition.face_encodings(picture)

    if len(encoding_picture1) > 0:
         encoding_picture = face_recognition.face_encodings(picture)[0]    
    else:
        encoding_picture = encoding_person1 + 1         
    #solved the problem of non-existing of any face in the frame
    #close the door if no one is there


                        #identifing
    # compare features
    r = face_recognition.compare_faces([encoding_person1], encoding_picture)

    if r[0] == True:
        data = str.encode ('1')
    else:
        r = face_recognition.compare_faces([encoding_person2], encoding_picture)
        if r[0] == True:
            data = str.encode ('2') 
        else:
            data = str.encode ('0')
            
    print (data)
    
    #sending data to arduino
    arduino.write(data)
    
    #quit on pressing Q key
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#close every thing
cap.release()
arduino.close()
cv2.destroyAllWindows()
