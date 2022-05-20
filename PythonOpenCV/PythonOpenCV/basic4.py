#change picture size
import cv2

url = "D:\OneDrive - KMITL\College Works\Zymurgy\Amanatsu\Code\OpenCV&Python-ComputerVision\opencvpython\PythonOpenCV\PythonOpenCV\image\cat.jpg"
img = cv2.imread(url, 0)
# 0 => gray skale
# 1 => color pic
imgresize = cv2.resize(img, (400,400)) #resize picture

cv2.imshow("Output", imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()