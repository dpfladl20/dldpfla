# 학생 클래스
# 속성 : 이름, 번호, 키
# 기능 : 학생정보보기, 학생정보입력, __init__ (학생정보입력)


class 학생:
    이름 = ''
    번호 = 0
    키= 0
    def 학생정보보기(self):
        print('이름:',self.이름, '번호:',self.번호,  '키:',self.키)
    def __init__(self,이름,번호,키):
        self.이름 = 이름
        self.번호 = 번호
        self.키 = 키
        self.학생정보입력(이름,번호,키)

    def 학생정보입력(self,이름,번호,키):
        self.이름 = 이름
        self.번호 = 번호
        self.키 = 키




# 사용예시
철수 = 학생('김철수',1,177.7)
영희 = 학생('박영희',2,155.5)
짱구 = 학생('신짱구',3,173.3)

철수.학생정보보기()     
영희.학생정보보기()
짱구.학생정보보기()     # 이름 : 신짱구, 번호 : 3, 키 : 173.3

짱구.학생정보입력('짱구',4,174.0)
짱구.학생정보보기()
영희.학생정보입력('영희',5,167.3)
영희.학생정보보기()
철수.학생정보보기() 
