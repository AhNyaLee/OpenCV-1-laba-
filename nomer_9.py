import cv2

cap=cv2.VideoCapture('http://192.168.1.133:8080/')
while (True):
   ok, img = cap.read()# если нам нужно  видео
   cv2.imshow('img', img)
   if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()