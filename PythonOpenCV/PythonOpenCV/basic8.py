# VDO Grayscale mode
from math import fabs
from pickle import TRUE
from tabnanny import check
import cv2

url = "D:\OneDrive - KMITL\College Works\Zymurgy\Amanatsu\Code\OpenCV&Python-ComputerVision\opencvpython\PythonOpenCV\PythonOpenCV\image\Video.mp4"

cap = cv2.VideoCapture(url)

while (cap.isOpened()):
    check, frame = cap.read() # get a picture from camera frame by frame

    if check == True : # check if the VDO is finished or not
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # convert color to grayscale
        cv2.imshow("Output", gray)
        if cv2.waitKey(1) & 0xFF == ord("e"): # convert to ascii code
            break
    else :
        break

cap.release() # clear ram
cv2.destroyAllWindows()