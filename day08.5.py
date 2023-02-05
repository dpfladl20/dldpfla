# opencv 모듈추가
# mdeiapipe 모듈추가

import cv2
import mediapipe as mp

# 이미지 띄우기

def Showimage(img_path):
    img = cv2.imread(img_path)
    cv2.putText(img, 'hello', 1, cv2.FONT_ITALIC, (0,50), 1)
    cv2.imshow(' ',img)
    cv2.waitKey(0)
    
Showimage('model.jpg')



# 동영상 띄우기
def ShowVideo(video_path):
    vc = cv2.VideoCapture(video_path)
    while True:
        success, img = vc.read()
        cv2.resize(img, tuple{1200,800})
        if success:
            cv2.imshow('',img)
        cv2.waitKey(20)

ShowVideo('model.mp4')


#웹캠 (얼굴찾기)