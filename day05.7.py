# # import 가 안되는 이유 = 설치가 안된 라이브러리(모듈) 또는 오타
# # 외부 모듈 설치 : pip install 모듈명
# import cv2

# 이미지 = cv2.imread('img1.png')     #이미지를 읽어줘
# cv2. imshow('title',이미지)         #보여줘

# cv2.waitKey(0)                      #무한대기


def cv_img(patch):
    이미지 = cv2.imread(patch)     #이미지를 읽어줘
    cv2. imshow('title',img)         #보여줘
    cv2.waitKey(0)   

cv_img('../fock.jpg')       # '.. <- 뒤로 한번 이동(폴더-폴더)



