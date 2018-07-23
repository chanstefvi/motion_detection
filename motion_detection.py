import cv2
import  numpy as np

cap = cv2.VideoCapture(0)
bckg_sub = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    mask = bckg_sub.apply(frame)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("original",frame)
    cv2.imshow("motion",mask)
    cv2.imshow("mo", res)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
