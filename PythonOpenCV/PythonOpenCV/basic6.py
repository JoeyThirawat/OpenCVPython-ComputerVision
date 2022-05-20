# turn on camera using OpenCV
import cv2

cap = cv2.VideoCapture(0)

while (True):
    ref, frame = cap.read() # get a picture from camera frame by frame
    cv2.imshow("Output", frame)

    if cv2.waitKey(1) & 0xFF == ord("e"): # convert to ascii code
        break

cap.release() # clear ram
cv2.destroyAllWindows()
