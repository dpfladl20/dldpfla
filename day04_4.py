 # 문자열을 저장하는 리스트
lst = []
num = 0

# 사용자에게 입력을 받아 리스트를 구성
# 1 : 추가하기 2 : 수정하기 3 : 삭제하기 4 : 전체보기

while True:
    num = int(input('1:추가, 2:수정, 3:삭제, 4:조회'))
    if num == 1:
        변수 = input('추가할 값을 입력하시오 >> ')
        lst.append(변수)
    elif num == 2:
        변수 = input('수정할 값을 입력하시오 >> ')
        lst.index(변수)
        변수2 = input('어떤 값으로 수정할까요? >> ')
        lst.append(변수2)
    elif num == 3:
        변수3 = input('삭제할 값을 입력하시오 >> ')
        lst.remove(변수3)
    elif num == 4:
        for i in lst:
            print(i)
    elif num == 0:
        break
    else:
        print('없는 번호입니다')
        
