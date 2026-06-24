import cv2
import numpy as np


img = cv2.imread('newspaper.jpg')

width, height = 640, 240 # 가로 60, 세로 240 으로 결과물 출력

src = np.array([[510,350], [1013,349], [1111,581], [458,577]], dtype=np.float32) # Input 4개 지정

dst = np.array([[0,0],[width,0],[width, height],[0, height]], dtype=np.float32)
# 좌상, 우상, 우하, 좌하 (시계 방향으로 4 지점 정의)

matrix = cv2.getPerspectiveTransform(src, dst) # Matrix 얻어옴
result = cv2.warpPerspective(img, matrix, (width, height)) # matrix에 대로 변환을 함.

cv2.imshow('img', img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()