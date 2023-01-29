
# 머신러닝 모듈
import sklearn
# 그래프 모듈
import matplotlib.pyplot as plt
# 수학/과학 계산 모듈
import numpy as np
# 다차원 데이터 모듈
import pandas as pd

from sklearn.linear_model import LinearRegression

print(sklearn.__verseion__)

'''
머신러닝(파이썬) : 데이터(정제) -> 기계학습 -> 예측결과 -> 머신러닝별 비교 후 선정
'''

# 데이터를 가져온다 csv
원본데이터 = pd.read_csv('sample.csv', encoding='cp949')
print(원본데이터.head())        # 잘 가져왔는지 상위 5개만 보기

# x(원인), y(결과)

x= 원본데이터.iloc[:,:-1].values
y= 원본데이터.iloc[:,-1].values

# [0,1,2]
# [[0],[1],[2]]

print(x)
print(y)

선형기계학습 = LinearRegression()
#fit을 사용하면 학습을 한다 (모델생성)
선형기계학습.fit(x,y)

# predict : 학습한 내용을 바탕으로 예측을 해보자
y_pred = 선형기계학습.predict(x)
print('예측한 y값:\n',y_pred)

print('ai예측값:',선형기계학습.predict(([4.5])))
print('ai예측값:',선형기계학습.predict(([6.5],[9])))

# 출력 print
plt.scatter(x,y, color='green')         # 원본 데이터는 점으로
plt.plot(x,y_pred, color='red')         # 예측 데이터는 선으로
plt.title('')                           # 제목 정해줘
plt.xlabel('hours')                     # x축 제목정해줘
plt.ylabel('corrsion rate')             # y축 제목정해줘
plt.show()                              # 보여줘



