# 일부 영역 색칠
import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)

# 특정 영역에 색칠
img[100:200, 200:300] = (255, 255, 255) # 흰색 사각형 세로 100~200, 가로 200~300 을 흰색으로

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()