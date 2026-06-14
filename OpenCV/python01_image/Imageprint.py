import cv2

img = cv2.imread('OpenCV/python01_image/img.jpg') # 해당 경로의 파일 읽어오기.
cv2.imshow('image', img) # (윈도우 창 이름, 이미지 변수)

# 앞에 key를 붙이면 사용자가 키보드로 입력한 값을 반환한다.
key = cv2.waitKey(0) # 지정된 시간(ms) 동안 사용자 키 입력 대기
print(key)

cv2.destroyAllWindows() # 모든 윈도우 창 닫기

