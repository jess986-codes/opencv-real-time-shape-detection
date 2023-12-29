limport cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lower_red = np.array([0, 0, 0])
    upper_red = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    cv2.imshow("Mask", mask)

    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break;


cap.release();
cv2.destroyAllWindows()
        