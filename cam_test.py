import cv2
import numpy as np
cap = cv2.VideoCapture(import cv2
import numpy as np
import serial
cap = cv2.VideoCapture(0)
one_person = 10
two_persons = 35
three_persons = 60
four_persons = 75
five_persons = 235

ser = serial.Serial('COM8' , 9600 , timeout = 0)

while(True):
    count=0
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(3,3),0)
    #ret,thresh = cv2.threshold(blur,50,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret,thresh=cv2.threshold(blur,30,255,cv2.THRESH_BINARY)
    
    cv2.imshow('frame',thresh)
    cv2.imshow('frame1',frame)
    
   
                            
    count=cv2.mean(thresh)
    k = count[0]
    k=int(k)
    
    k=255-k
    if k<one_person:
        k=9
    elif one_person<=k< two_persons:
        k=0
    elif two_persons<= k <three_persons:
        k=1
    elif three_persons<= k <four_persons:
        k=2
    else :
        k=3
    
    k=str(k)
    print(k)

    ser.write(k)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

cap.release()
cv2.destroyAllWindows()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
)

while(True):
    count=0
    ret,frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
