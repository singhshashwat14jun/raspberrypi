import picamera
from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy
import cv2


cap=PiCamera()
rc=PiRGBArray(cap,(320,240))
cap.framerate = 8

while True:
    for image in cap.capture_continuous(rc, format="bgr", use_video_port=True, resize=(320, 240)):
        frame = image.array
        cv2.imshow('frame', frame)
        cv2.waitKey(10)
        rc.truncate(0)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
