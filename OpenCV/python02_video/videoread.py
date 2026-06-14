# 동영상 파일 출력
import cv2

cap = cv2.VideoCapture('OpenCV/python02_video/video.mp4') # 동영상 파일 읽어오기
while cap.isOpened(): # 동영상 파일이 정상적으로 열렸는지 확인
    ret, frame = cap.read() # 동영상에서 프레임 읽어오기 (ret: 프레임 읽기 성공 여부, frame: 읽어온 프레임)
    if not ret: # 프레임을 읽어오지 못하면 반복문 종료
        print('더 이상 가져올 프레임이 없습니다.')
        break
    
    cv2.imshow('video', frame) # 프레임 출력
    if cv2.waitKey(30) & 0xFF == ord('q'): # 30ms마다 키 입력 대기, 'q' 키를 누르면 종료 / waitKey()가 영상 속도를 조절한다.
        print('사용자 입력에 의해 종료되었습니다.')
        break
    
cap.release() # 동영상 파일 해제
cv2.destroyAllWindows() # 모든 윈도우 창 닫기