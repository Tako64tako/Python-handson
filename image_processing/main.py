import cv2

filename = "/image/Lenna.png"

gry = cv2.imread(filename, 0)
cv2.imwrite("/image/Lenna_gray.png", gry)
