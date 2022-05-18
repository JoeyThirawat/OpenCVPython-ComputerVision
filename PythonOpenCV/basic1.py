import cv2

img = cv2.imread("D:\OneDrive - KMITL\College Works\Zymurgy\Amanatsu\Code\OpenCV&Python-ComputerVision\code\PythonOpenCV\image\cat.jpg")
# imread = image read

print(type(img.ndim)) # ndim = n-dimensions => numpy array
# img => numpy array
# type = cheak type of data
print(img)