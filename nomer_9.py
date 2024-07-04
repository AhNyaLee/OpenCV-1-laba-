import cv2
cap=cv2.VideoCapture('http://[2a00:1fa1:1205:b286:0:51:6615:1701]:8080')
while True:
    ok, img = cap.read()
    if not ok:
        print("Не удалось прочитать кадр")
        break
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()