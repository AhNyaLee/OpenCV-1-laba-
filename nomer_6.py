import cv2
cap=cv2.VideoCapture(0)
ok, img = cap.read()#Если нужен один кадр
while (True):
   # ok, img = cap.read()# если нам нужно  видео
   cv2.rectangle(img, (15, 25), (200, 100), (0, 0, 255), 1)
   cv2.imshow('img', img)
   if cv2.waitKey(1) & 0xFF == 27:
        break
#cv2.rectangle(img, pt1, pt2, color[, thickness[,lineType[,shift]]])  рисуем крест
