import cv2
import serial
# ser = serial.Serial('/dev/cu.usbmodem1101',9600)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
d = 69
# cap = cv2.VideoCapture('vid.mp4')
while True:
    # d = ser.readline().strip()
    # print(d)
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if d != '0':
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(img, f'intrusion detected', (x, y-8), color=(0, 0, 255), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()