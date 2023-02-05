import cv2
import mediapipe as mp
# pip install mediapipe

# 만약에 os권한문제로 설치가 안될경우
'''
0. 파이썬 실행 중인지 체크한다 (만약 실행중이면 중지버튼 눌러 중단한다)
1. anaconda prompt를 관리자권한으로 시행
2. python -m pip install --upgrade pip 를 업그레이드 시켜줌
3. 재설치
'''


#동영상 읽어줘 ▼
'''
만약에 웹캠이면 VideoCapture 에 0을 넣고, 맨 밑 waitKey 에 1을 넣는다
'''

# img = cv2.imread('person.jpg')
# cv2.imshow('title',img)
# cv2.waitKey(0)

cap = cv2.VideoCapture('person.mp4')            # 0 으로 입력하면 웹캠
mp_fd = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
fd = mp_fd.FaceDetection(0.9)              # 정확도 조정

# 무한반복 (동영상 == 빠르게 여러이미지를 보여주기)
while True:
    # 읽기성공여부, 동영상을자른이미지
    success, img = cap.read()
    # 동영상을 성공적으로 읽었으면 보여주기 전에 얼굴을 찾는다
    if success:
        from_bgr_to_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)       # 얼굴찾기 정확도 향상을 위해서 BGR -> RGB로 변환      
        face = fd.process(from_bgr_to_rgb)      # 얼굴찾기

        if face.detections:
            # 얼굴을 찾았다 == > 사람 얼굴을 찾은 다음 하고싶은 동작
            # 사용할 함수 추가
            for id, detection in enumerate(face.detections):
                # mp_draw.draw_detection(img, detection)              #찾은 얼굴을 사각형 표시, mediapipe 얼굴표시
                fd_box = detection.location_data.relative_bounding_box
                box = int(fd_box.xmin * img.shape[1]), int(fd_box.ymin * img.shape[0]), \
                    int(fd_box.width * img.shape[1]), int(fd_box.height * img.shape[0])
                cv2.rectangle(img,box,(255,0,255),2)
                cv2.putText(img, f'{round(detection.score[0]*100,1)}%', (box[0],box[1]), cv2.FONT_ITALIC, 1, (255,0,255),2)

        cv2.imshow('tltle',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
