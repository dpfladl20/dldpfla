# 출력 print(123)
# 변수와 자료형
변수 = '저장공간(문자열형)'
정수형 = 1234
실수형 = 1.234

변수 = '문자열형'

print(정수형)
print(실수형)
print(변수)
print('내가 저장하고 싶은 값',변수)
print('내가 저장하고 싶은 값:{},{}'.format(변수,실수형))
print(f'내가 저장하고 싶은 값:{변수},{실수형}')

# 리스트, 튜플, 세트, 딕셔너리 (하나의 변수에 여러개의 값을 저장하려고)
lst = [1,2,3,'hello',4,5,6]
tup = (1,2,3,'hello',4,5,6)     # 수정 X
s = {1,2,3,'hello',4,5,6}       # 중복 X
dic = {'a':'에이','b':'비','c':'씨',1:1.0}       # 키를 고정

# 리스트 추가하려면
lst.append('맨 뒤에 추가')
print(lst)

# 리스트 삭제하려면 (맨뒤에꺼)
lst.pop()
print(lst)

# 리스트 전체 조회
for item in lst:
    print(item, end=' ')
print()

dic['추가할키워드'] = '추가할 값'   # 추가
dic[1] = '일'    # 수정(기존에 있는 키워드 수정)
print(dic)

print(lst[0])   # 0 값부터 보여줌
print(dic['a'])  # 지정한 키워드를 보여줌

# 딕셔너리 전체 조회
for i in dic:
    print(dic.get(i), end= ' ')
print()

# 입력 (변수가 필요)
변수 = input('입력할 문자열을 알려주세요>> ')
정수형 = int(input('입력할 정수를 알려주세요>> '))
print('내가 입력할 문자열:',변수,'\n내가 입력할 정수:',정수형)

# 조건/반복문
if 정수형 < 10:
    print('10보다 작네요')
elif 정수형 < 100:
    print('100보다 작네요')
else:
    print('100 이상입니다')

# 반복문
for i in range(1,5):
    print('5번 반복',i)

for i in lst:
    if i == 'hello':
        print('hello 찾음')
        break          # 반복문을 즉시 종료

