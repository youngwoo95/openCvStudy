import cv2
import numpy as np

# 세로 480 x 가로 640 x 채널 3 (BGR) 에 해당하는 스케치북 만들기
img = np.zeros((480, 640, 3), dtype=np.uint8)
# img[:] = (255, 255, 255) # 전체 공간을 흰색으로 채우기
# img = np.full((480, 640, 3), (255, 255, 255), dtype=np.uint8) # 전체 공간을 흰색으로 채우기

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

