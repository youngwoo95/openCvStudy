# 사각형 그리기
import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (0, 255, 0) # BGR 노란색 : Yello, 색깔
THICKNESS = 10 # 선의 두께

cv2.rectangle(img, (100, 100), (200, 200), COLOR, THICKNESS, cv2.LINE_AA) # 속이 빈 원
# 그릴 위치, 왼쪽 위 좌표, 오른쪽 아래 좌표, 색깔, 두께
cv2.rectangle(img, (300, 100), (400, 200),COLOR, cv2.FILLED, cv2.LINE_AA) # 속이 꽉찬 원


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()