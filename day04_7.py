import matplotlib.pyplot as plt         #그래프 그려주는 라이브러리(부속품)


# 문제
시험점수 = [71, 85, 77, 81, 99, 23, 55, 100, 0]
_80점이상 = []

# 1. 시험점수 중 80점 이상만 _ 80점이상 리스트로 옮기고
for i in 시험점수:
    if i >= 80:
        _80점이상.append(i)

# 2. 80점 이상의 갯수를 구한다
print(len(_80점이상),'명')


# 데이터의 시각화
plt.title(test)
plt.hist(시험점수)
plt.show()
