## Haar Cascades by https://github.com/andrewssobral/vehicle_detection_haarcascades
## Project By Saswat Samal : www.saswatsamal.me

# importing openCV library
# install it by: pip install opencv-python in CMD
import cv2

# Haar Cascades Source Car.xml
cascade_src = 'cars.xml'

#Video Capture by your Default Webcam.
cap = cv2.VideoCapture(0)

car_cascade = cv2.CascadeClassifier(cascade_src)


while True:
    ret, img = cap.read()
   
    if (type(img) == type(None)):
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 2)


    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
    
    cv2.imshow('video', img)
   
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
