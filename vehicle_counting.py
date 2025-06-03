import cv2
import glob
from vehicle_detector import VehicleDetector
import threading
import time


def web_out():
    # Load Veichle Detector
    vd = VehicleDetector()
    cv2.ocl.setUseOpenCL(True)
    # Load images from a folder
    # images_folder = glob.glob("images/*.jpg")

    vehicles_folder_count = 0
    # vid = cv2.VideoCapture(0)
    vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    vid.set(cv2.CAP_PROP_FPS, 30)
    vid.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

    while True:
        ret, frame = vid.read()
        # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        if ret:
            # Display the resulting frame
            # cv2.imshow('frame', img)
            vehicle_boxes = vd.detect_vehicles(frame)
            vehicle_count = len(vehicle_boxes)

            for box in vehicle_boxes:
                x, y, w, h = box

                cv2.rectangle(frame, (x, y), (x + w, y + h), (25, 0, 180), 3)

                cv2.putText(frame, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

            cv2.imshow("Cars", frame)
            # time.sleep(0.1)
            # cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break


# vid.release()
# cv2.destroyAllWindows()
# print("Total current count", vehicles_folder_count)
webcam_thread = threading.Thread(target=web_out)
webcam_thread.start()
