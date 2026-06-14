# 카메라 출력
import cv2
cap = cv2.VideoCapture(0) # DeviceId : 0번 카메라 장치 열기 (노트북 내장 카메라가 0번, 외장 카메라가 1번 등으로 할당됨)

if not cap.isOpened(): # 카메라 장치가 정상적으로 열렸는지 확인
    print('카메라를 열 수 없습니다.')
    exit()

while cap.isOpened(): # 카메라 장치가 정상적으로 열렸는지 확인
    ret, frame = cap.read() # 카메라에서 프레임 읽어오기 (ret: 프레임 읽기 성공 여부, frame: 읽어온 프레임)
    if not ret: # 프레임을 읽어오지 못하면 반복문 종료
        print('카메라에서 프레임을 가져올 수 없습니다.')
        break
    
    cv2.imshow('camera', frame) # 프레임 출력
    if cv2.waitKey(1) & 0xFF == ord('q'): # 1ms마다 키 입력 대기, 'q' 키를 누르면 종료 / waitKey()가 영상 속도를 조절한다.
        print('사용자 입력에 의해 종료되었습니다.')
        break
    
cap.release() # 카메라 장치 해제
cv2.destroyAllWindows() # 모든 윈도우 창 닫기