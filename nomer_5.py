import cv2
frame = cv2.imread("1.png")
resized_frame = cv2.resize(frame, (500, 400), interpolation=cv2.INTER_AREA)
hsv = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2HSV)
while True:
    cv2.imshow("Image", hsv)
    cv2.imshow("Image original", resized_frame)
    if cv2.waitKey(25) == 27:
        break