import cv2

img_color = cv2.imread('OpenCV/python01_image/img.jpg', cv2.IMREAD_COLOR) # 해당 경로의 파일 읽어오기.
img_gray = cv2.imread('OpenCV/python01_image/img.jpg', cv2.IMREAD_GRAYSCALE) # 흑백 이미지로 읽기
img_unchanged = cv2.imread('OpenCV/python01_image/img.jpg', cv2.IMREAD_UNCHANGED) # 알파 채널 포함하여 읽기

cv2.imshow('img_color', img_color)
cv2.imshow('img_gray', img_gray)
cv2.imdshow('img_unchanged', img_unchanged)

cv2.waitKey(0)
cv2.destroyAllWindows()


'''
읽기 옵션
cv2.IMREAD_COLOR : 컬러 이미지로 읽기 (기본값), 투명 영역은 무시
cv2.IMREAD_GRAYSCALE : 흑백 이미지로 읽기
cv2.IMREAD_UNCHANGED : 알파 채널(투명 영역) 포함하여 읽기
'''
