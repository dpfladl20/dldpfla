# 머신러닝
# pip install scikit-learn

import sklearn
print(sklearn._version_)

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


print('사이킷런 버전:',sklearn._version_)

운동시간 = [[1],[2],[3],[4],[5]]
근육량 = [[1],[2],[3],[3.5],[3.5]]

lin = LinearRegression()

# 인공지능 학습 fit(x,y)
lin.fit(운동시간,근육량)

# 학습 기반으로 예측
근육량예측 = lin.predict(운동시간)
print(근육량예측)
print(lin.predict([[2.5]]))
plt.scatter(운동시간, 근육량, color='blue')
plt.plot(운동시간,근육량예측, color='green')
plt.show()

