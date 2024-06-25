import cv2
def cross(img):
   # Получаем размеры изображения
   width = img.shape[1]
   height = img.shape[0]
   # Расчет координат прямоугольника(первого вертикального), чтобы он был по центру
   rect_top_left = ((width - 50) // 2, (height + 10) // 2)
   rect_bottom_right = (rect_top_left[0] + 30, rect_top_left[1] + 100)
   # Рисуем прямоугольник (первого вертикального)
   cv2.rectangle(img, rect_top_left, rect_bottom_right, (0, 0, 255), 1)
   # Расчет координат прямоугольника(горизонтальный), чтобы он был по центру
   rect_top_left = ((width - 200) // 2, (height - 50) // 2)
   rect_bottom_right = (rect_top_left[0] + 200, rect_top_left[1] + 30)
   # Рисуем прямоугольник (горизонтальный)
   cv2.rectangle(img, rect_top_left, rect_bottom_right, (0, 0, 255), 1)
   # Расчет координат прямоугольника(второго вертикального), чтобы он был по центру
   rect_top_left = ((width - 50) // 2, (height - 250) // 2)
   rect_bottom_right = (rect_top_left[0] + 30, rect_top_left[1] + 100)
   # Рисуем прямоугольник (второго вертикального)
   cv2.rectangle(img, rect_top_left, rect_bottom_right, (0, 0, 255), 1)
cap=cv2.VideoCapture(0)
#ok, img = cap.read()#Если нужен один кадр
while (True):
   ok, img = cap.read()# если нам нужно  видео
   cross(img)
   cv2.imshow('img', img)
   if cv2.waitKey(1) & 0xFF == 27:
        break
#cv2.rectangle(img, pt1, pt2, color[, thickness[,lineType[,shift]]])  рисуем крест
