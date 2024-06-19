import cv2
nomber_img=int(input("Выберите номер картинки от 1 до 3"))
if nomber_img==1:
    image = cv2.imread("C:/Users/User/Pictures/e6044cb0b978ce39ff76b57402ebd1de.jpeg", cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow("Image 1", cv2.WINDOW_NORMAL)
    cv2.resize(image, (300, 200), interpolation=cv2.INTER_AREA)
    while True:
        cv2.imshow("Image 1", image)
        if cv2.waitKey(25) == 27:
            break
elif nomber_img==2:
    image = cv2.imread("C:/Users/User/Pictures/1.png", 8)
    cv2.namedWindow("Image 2", cv2.WINDOW_KEEPRATIO)
    cv2.setWindowProperty("Image 2", cv2.WND_PROP_ASPECT_RATIO, 1.0)
    while True:
        cv2.imshow("Image 2", image)
        if cv2.waitKey(25) == 27:# Закрытие окна происходит при нажатии на esc
            break
else:
    image = cv2.imread("C:/Users/User/Pictures/2.jpg", 0x221111)
    cv2.namedWindow("Image 3", cv2.WINDOW_AUTOSIZE)
    cv2.setWindowProperty("Image 3", cv2.WND_PROP_ASPECT_RATIO, 0.0)
    while True:
        cv2.imshow("Image 3", image)
        if cv2.waitKey(25) == 27:  # Закрытие окна происходит при нажатии на esc
            break
cv2.destroyAllWindows()
