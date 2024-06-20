import cv2
n=int(input("1 или 2"))
cap=cv2.VideoCapture(r'video5444892193334510796.mp4',cv2.CAP_ANY)
if n==1 :
    while True:
        ret, frame =cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if not(ret):
            break
        resize=cv2.resize(gray, (300, 400))
        cv2.imshow('video',resize)
        cv2.setWindowProperty('video', cv2.WND_PROP_TOPMOST, 1)
        if cv2.waitKey(4) & 0xFF==27:
            break
if n==2:
    while True:
        ret, frame = cap.read()
        if not (ret):
            break
        cv2.imshow('video', frame)
        cv2.setWindowProperty('video', cv2.WND_PROP_TOPMOST, 1)
        if cv2.waitKey(4) & 0xFF == 27:
            break