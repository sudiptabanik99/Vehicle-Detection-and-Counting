import cv2

print(cv2.cuda.getCudaEnabledDeviceCount())
vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
vid.set(cv2.CAP_PROP_FPS, 30)
vid.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Check if the webcam is opened correctly

while True:
    ret, frame = vid.read()
    # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

vid.release()
cv2.destroyAllWindows()