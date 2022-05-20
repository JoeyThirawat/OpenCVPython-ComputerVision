import cv2

url = "D:\OneDrive - KMITL\College Works\Zymurgy\Amanatsu\Code\OpenCV&Python-ComputerVision\opencvpython\PythonOpenCV\PythonOpenCV\image\cat.jpg"
img = cv2.imread(url, 0)
imgresize = cv2.resize(img,(400,400))
cv2.imshow("My Cat", imgresize)

cv2.imwrite("output.jpg", imgresize)

cv2.waitKey(0)
cv2.destroyAllWindows()