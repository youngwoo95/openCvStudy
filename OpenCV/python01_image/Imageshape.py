import cv2

img = cv2.imread('OpenCV/python01_image/img.jpg') # 해당 경로의 파일 읽어오기.
print(img.shape) # 이미지의 높이, 너비, 채널 수 반환

cv2.imshow('image', img) # (윈도우 창 이름, 이미지 변수)
cv2.waitKey(0) # 지정된 시간(ms) 동안 사용자 키 입력 대기
cv2.destroyAllWindows() # 모든 윈도우 창 닫기


'''
Shape
이미지의 Hegight, Width, Channel 수를 반환하는 속성
'''
