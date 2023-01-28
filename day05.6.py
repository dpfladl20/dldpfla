# 외부 함수를 사용하는 방법 : import
# 모듈 : 부품명칭

# import 모듈명
# import 모듈명 as 별명
# ㄴ 모듈명이 너무 긴 경우 별명을 만들어서 짧게사용

# from 모듈명 import 함수명

# 모듈명을 plt로 사용
import matplotlib.pyplot as plt
# 모듈 중에 front_manger 와 rc 부분만 가져옴
from matplotlib import font_manager, rc

font = font manager.FontProperties(fname='HMKMRHD.ttc').get_name()
rc('font',family=font)


lst = [10,20,12,31,41,90,66,11,44,88]
plt.title('분포도')
plt.xlabel('점수')
plt.ylabel('갯수')
plt.hist(lst)                 # 막대그래프로 그려줘
plt.show()                    # 보여줘

