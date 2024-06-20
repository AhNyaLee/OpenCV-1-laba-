import cv2
def ReadIPWriterTofile():
    camera = cv2.VideoCapture(0)
    w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcce=cv2.VideoWriter_fourcc(*'mp4v')
    camera_writer=cv2.VideoWriter("output.mp4",fourcce,25,(w,h))
    while (True):
        ok, img = camera.read()
        cv2.imshow('img', img)
        camera_writer.write(img)
        if cv2.waitKey(1) & 0xFF==27:
            break
    camera.release()
    cv2.destroyAllWindows()

ReadIPWriterTofile()
