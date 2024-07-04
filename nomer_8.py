import cv2
def cross(img):
    # Получаем размеры изображения
    width = img.shape[1]
    height = img.shape[0]
    # Расчет координат прямоугольников
    rects = [
        (((width - 50) // 3, (height + 500) // 3), (30, 100)),
        (((width - 300) // 3, (height + 450) // 3), (200, 30)),
        (((width - 50) // 3, (height + 150) // 3), (30, 100))
    ]
    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]

    for i, (top_left, size) in enumerate(rects):
        color = colors[i % len(colors)]
        cv2.rectangle(img, top_left, (top_left[0] + size[0], top_left[1] + size[1]), color, -1)
        cv2.rectangle(img, top_left, (top_left[0] + size[0], top_left[1] + size[1]), (0, 0, 255), 1)
img = cv2.imread('2.jpg')
cross(img)
cv2.imshow("Image 2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
