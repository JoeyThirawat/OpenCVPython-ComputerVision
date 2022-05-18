import cv2

img = cv2.imread("D:\OneDrive - KMITL\College Works\Zymurgy\Amanatsu\Code\OpenCV&Python-ComputerVision\code\PythonOpenCV\image\cat.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()