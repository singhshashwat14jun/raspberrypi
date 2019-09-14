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

        blur = cv2.GaussianBlur(frame, (5, 5), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        lower_red1 = np.array([0, 100, 0])
        upper_red1 = np.array([5, 255, 255])
        lower_red2 = np.array([170, 100, 0])
        upper_red2 = np.array([180, 255, 255])

        lower_blue = np.array([38, 36, 0])
        upper_blue = np.array([121, 255, 255])

        lower_green = np.array([50, 60, 60])
        upper_green = np.array([95, 255, 255])

        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])

        maskr1 = cv2.inRange(hsv, lower_red1, upper_red1)
        maskr2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask1 = maskr1 + maskr2
        # red = cv2.bitwise_and(frame, frame, mask=mask1)

        mask2 = cv2.inRange(hsv, lower_blue, upper_blue)
        # blue = cv2.bitwise_and(frame, frame, mask=mask2)

        mask3 = cv2.inRange(hsv, lower_green, upper_green)
        # green = cv2.bitwise_and(frame, frame, mask=mask3)

        mask4 = cv2.inRange(hsv, lower_yellow, upper_yellow)
        # yellow = cv2.bitwise_and(frame, frame, mask=mask4)

        _, contours, _ = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours:
            area1 = cv2.contourArea(contour)
            # print(area)
            if area1 > 2000:
                cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)
                # find centre and put text on it

        _, cnts, _ = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for cnt in cnts:
            area2 = cv2.contourArea(cnt)
            # print(area)
            if area2 > 2000:
                cv2.drawContours(frame, cnts, -1, (255, 0, 0), 3)
                # find centre and put text on it

        _, cns, _ = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for cn in cns:
            area3 = cv2.contourArea(cn)
            # print(area)
            if area3 > 2000:
                cv2.drawContours(frame, cns, -1, (0, 255, 0), 3)
                # find centre and put text on it

        _, cs, _ = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for c in cs:
            area4 = cv2.contourArea(c)
            # print(area)
            if area4 > 2000:
                cv2.drawContours(frame, cs, -1, (0, 0, 0), 3)
                # find centre and put text on it

        cv2.imshow('frame', frame)
        cv2.waitKey(10)
        rc.truncate(0)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
