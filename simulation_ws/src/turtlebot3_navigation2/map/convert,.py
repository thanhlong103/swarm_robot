import cv2
img = cv2.imread("sim_map.pgm", -1)
print(img.shape)

cv2.imwrite("sim_map.png", img)