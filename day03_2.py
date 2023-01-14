# 반복문 (while, for)
# for를 사용해서 hello 3번 하기

for 임시변수 in range(3):
    print('hello')

# 임시변수 : while 에서 i를 값으로 사용 ==> 임시변수

i = 0
while i < 3:
    print(i,'번째 hello')
    i+=1

for j in range(3):
    print(j, '번째 hello')


# i = 1
for i in range(1, 4):
    print(i, '번째 hello')


# range(3) ==> range(0, 3) (0~2까지)
# range(1, 4) ==> 1~4 전까지 (즉, 1~3까지 표기됨)

# 1월~12월 출력

# i = 1
# for i in range(1, 13):
#     print(i,'월')

# for i in range(1, 101, 7):
#     print(i)

# for j in range(0, 11, 2):
#     print(j) 


# 문제 
'''
5
4
3
2
1

'''
i = 5
for i in range(6):
    print(i)

i=  5
for i in range(5, 0, -1):
    print(i)

for i in reversed(range(1, 6)):
    print(i)


#문제2
'''
양의 정수 1개를 입력받아서
1 부터 입력한 숫자까지 합계를 알려주는 프로그램

'''
count = int(input('양의 정수를 입력하시오>> '))
sum = 0 # 변수 활용을 위한 공간을 마련하는게 중요!!!
for i in range(1, count+1):
    sum += i
print(sum)
    


#문제 3
# num1 = 1
# num2 = 2
# print(num1, num2)
# backup = 0
# backup = num1
# num1 = num2
# num2 = backup

