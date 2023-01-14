#1 
# # 횟수를 입력받아서 그 수만큼 hello 출력하는 프로그램

# 횟수 = int(input('횟수를 입력하세요>> '))
# i = 0

# while 1 < 횟수:
#     i+=1
#     print(i,'번째 hello')
    

# 2
# 1~100 사이에서 7의 배수만 출력하는 프로그램 (while 안에 if 사용)

# i = 1
# while i < 101 :
#     if i % 7 == 0:
#         print(i)
#     i += 1
    
#3 
# 커피 한잔에 300원, 금액을 입력하여 몇잔의 커피와 잔돈이 얼마가 남는지 출력
# 커피잔수 = 0
# price = 300
# 금액 = int(input('금액은 얼마 인가요 >> '))

# while 금액 >= price:
#     금액 -= price
#     커피잔수 += 1

#     print('커피',커피잔수,'잔, 잔돈',금액,'원')

# =======================================
# 자료형 / 변수
'''
변수 : 저장공간
    - 대입연사자를 사용 =
    - 자주 변경될 것 같은 혹은 자주 사용될 것 같은 값은 미리 저장해서 관리한다
    - 변수에 있는 값만 수정하면 변수를 사용한 코드는 일괄 수정
    - 변수명 1 = '값'
    - 변수명1 이라는 공간이 생기면서 값이라는 데이터가 들어간다

자료형(type) : 데이터의 타입
    - str , int , float
    - 오류검출, 실수검출, 의도명확화 
    - 뺄셈으로 사용하려는지 or 핸드폰 번호로 사용하려고 하는지 컴퓨터는 알수 없다
    - 자료형 변환
        (1) '33-4' ==> int('33-4') ==> 29
        (2) 변환하고자 하는 자료형으로 감싸준다 float(정수변수)
        (3) '나는 문자열이지' ==> int('나는 문자열이지') ===> 컴파일 오류
        (4) 데이터가 맞아야지만 타입 변환이 가능

'''
# 변수1 = 123
# 변수2 = '문자열'
# int(변수1)
# int(변수2)    #변환하고자 하는 자료형과 호환가능한 값만 변환 가능

# # 출력
# print('안녕')
# print (3.14)
# print(변수2)
# print('안녕',변수2)
# print('안녕 {},{},{}'.format(변수2, 변수1, 314))
# print(f'안녕 {변수2},{변수1},{314}')

# 조건문/반복문
'''
if 조건식:
    조건식이 True 일때만 실행할 문장 1

조건문은 실행후에 밑으로 내려오지만 

while 조건식:
    조건식이 True 일때만 실행할 문장1
    조건식이 True 일때만 실행할 문장2
반복문은 실행되면 위로 다시 올라감 (위 -> while으로 다시 올라가서 조건식 검사부터 다시 시작)


'''
#if ~ elif ~ else

i = 3
if i == 3:
    print('조건이 맞네요')
    print('조건이 맞으면 이 문장은 실행됩니다')
print('조건문이 끝났습니다')

i = 0
while i < 3:
    print('반복문이 실행됩니다')
    print('조건이 맞는 동안에는 이 문장이 실행되겠네요',i)
    i +=1
print('반복문이 끝났습니다')


