import cv2

print("cv2.__version__")
img = cv2.imread('img.jpg')

cv2.imshow('img', img)