import cv2
nomber_img=int(input("Выберите номер картинки от 1 до 3"))
if nomber_img==1:
    image = cv2.imread("e.svg", cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow("Image 1", cv2.WINDOW_NORMAL)
    while True:
        cv2.imshow("Image 1", cv2.resize(image, (300, 200), interpolation=cv2.INTER_AREA))
        cv2.setWindowProperty("Image 1", cv2.WND_PROP_TOPMOST, 1)
        if cv2.waitKey(25) == 27:
            break
elif nomber_img==2:
    image = cv2.imread("1.png", 8)
    cv2.namedWindow("Image 2", cv2.WINDOW_KEEPRATIO)
    cv2.setWindowProperty("Image 2", cv2.WND_PROP_ASPECT_RATIO, 1.0)
    while True:
        cv2.imshow("Image 2", image)
        if cv2.waitKey(25) == 27:
            break
else:
    image = cv2.imread("2.jpg", 0x221111)
    cv2.namedWindow("Image 3", cv2.WINDOW_AUTOSIZE)
    cv2.setWindowProperty("Image 3", cv2.WND_PROP_ASPECT_RATIO, 0.0)
    while True:
        cv2.imshow("Image 3", image)
        if cv2.waitKey(25) == 27:  # Закрытие окна происходит при нажатии на esc
            break
cv2.destroyAllWindows()
