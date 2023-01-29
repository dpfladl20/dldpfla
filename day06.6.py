


# 문제 1: 머신러닝을 사용해서 300명이 방문했을 때 판매량을 예측해 보세요

import sklearn
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

원본데이터 = pd.read_csv('kyobo.csv', encoding='cp949')

x= 원본데이터.iloc[:,:-1].values
y= 원본데이터.iloc[:,-1].values

test = LinearRegression()
test.fit(x,y)
y_pred = test.predict(x)
y_300 = test.predict([[300]])
print('y_result:\n',y_pred)
print('300명이 오면:\n',y_300)

plt.scatter(x,y, color='blue')
plt.plot(x,y_pred, color='red')
plt.title('visitors of sales volume')
plt.xlabel('visitors')
plt.ylabel('sales volume')
plt.show()
