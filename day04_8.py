# 튜플 tuple
# tuple = ()
# 튜플 : 추가할 수 없다 (고정)

menu = ('돈까스','순두부','김밥')
print(menu[0])
print(menu[1])
print(menu[2])

# 전체 조회
for i in menu:
    print(i)


name1 = ' '
name2 = ' '
name3 = ' '

name1, name2, name3 = menu
name1, name2, name3 = ('안녕하세요','반갑습니다','잘부탁해요')    # 분할해서 대입 가능

print(name1, name2, name3)
