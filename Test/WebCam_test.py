import cv2,time

video = cv2.VideoCapture(0)
address = "http://192.168.0.106:4747/video"
video.open(address)

while True:
    check,frame = video.read()
    cv2.imshow("Video",frame)
    key = cv2.waitKey(1)
video.release()
cv2.destroyAllWindows()