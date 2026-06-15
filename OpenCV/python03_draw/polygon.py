# 다각형 그리기
import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (0, 0, 255) # BGR 빨간색 : Red, 색깔
THICKNESS = 10 # 선의 두께

pts1 = np.array([[100, 100], [200, 100], [100, 200]])
pts2 = np.array([[200, 100], [300, 100], [300, 200]])


# 그릴곳, 점들의 좌표, 닫힘 여부 상태, 색깔, 두께, 선 종류
#cv2.polylines(img, [pts1], True, COLOR, THICKNESS, cv2.LINE_AA) 
cv2.polylines(img, [pts1, pts2], True, COLOR, THICKNESS, cv2.LINE_AA) # 속이 빈 다각형

pts3 = np.array([[[100, 300], [200, 300], [100, 400]], [[200, 300], [300, 300], [300, 400]]])
# 그릴곳, 점들의 좌표, 색깔, 선 종류
cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA) # 속이 꽉찬 다각형



cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()