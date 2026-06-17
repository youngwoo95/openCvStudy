# 파일저장
import cv2

img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE) # 흑백으로 이미지 불러오기



cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


result = cv2.imwrite('grayImg.jpg', img)
if result:
    print('이미지 저장에 성공하였습니다.')
else:
    print('이미지 저장에 실패하였습니다.')