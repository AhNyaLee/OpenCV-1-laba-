import cv2
video=cv2.VideoCapture(r'video5444892193334510796.mp4',cv2.CAP_ANY)
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcce=cv2.VideoWriter_fourcc(*'mp4v')
video_writer=cv2.VideoWriter("writervideo.mp4",fourcce,25,(w,h))
while (True):
    ret, frame = video.read()
    if not (ret):
        break
    cv2.imshow('video', frame)# Мы хотим отображать то видео, которое записываем в другой фалй
    #video_writer.write(frame) здесь пишем, если хотим полностью записать видео, не зависимость от того, когда мы нажали esc
    cv2.setWindowProperty('video', cv2.WND_PROP_TOPMOST, 1)
    if cv2.waitKey(4) & 0xFF == 27:
        break
    video_writer.write(frame)# Пишем здесь, если мы хотим записать ровно до того момента как нажали esc