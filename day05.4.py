# 3개를 더하기, 빼기, 곱하기, 나누기
# + , - , * , / : 2개만 할 수 있음(기본)

def 더하기(num1,num2,num3):
    print(num1+num2+num3)

print(1+2)
더하기(1,2,3)

# 빼기
def 빼기(num1,num2,num3):
    print(num1-num2-num3)

빼기(3,2,1)

# 곱하기
def 곱하기(num1,num2,num3):
    print(num1*num2*num3)

곱하기(1,2,3)

# 나누기
def 나누기(num1,num2,num3):
    print(num1/num2/num3)

나누기(10,2,2)

# return : 함수의 결과를 활용할 수 있게 해준다

def 절대값더하기(a, b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    return a+b     # return 옆에 있는 값이 사용한 곳으로 전달?


결과1 = 절대값더하기(3,7)
결과2 = 절대값더하기(-4,결과1)
print(결과2)
print(절대값더하기(-1,-1))

