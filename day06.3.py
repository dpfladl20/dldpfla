# 파일 읽고 쓰기

def 파일쓰기():
    # 파일 만들고 쓰기(txt) : 이미 파일이 있으면 쓰기만 함
    f = open('sample.txt', 'w+', encoding='UTF-8')      # w : 쓰기
    f.write('안녕하세요, 반갑습니다\n')         #\m : 엔터키, 한줄바꾸기
    f.close()

# 파일 읽기(txt)
def 파일읽기(filepath):
    f = open('sample.txt','r', encoding='UTF-8')
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line, end=' ')
    f.close()

# 파일 추가쓰기(txt) : 'a+'
def 파일추가쓰기(filepath):
    f = open('sample.txt', 'a+', encoding='UTF-8')
    f.write('다시 만나요')
    f.close()


