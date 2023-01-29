# csv파일 (구 엑셀)
# import : 외장모듈(함수나 클래스) 사용
import csv

def csv파일생성():
    f= open('kyobo.csv','w',newline='')
    wr = csv.writer(f)
    wr.writerow(['년도','인구'])
    f.close()


def csv파일이어쓰기():
    f= open('sample.csv','a',newline='')
    ad= csv.writer(f)       # ---> 내용추가 'a', 'ad (줄임말)'
    ad.writerow([2,'년도','인구'])
    f.close()

csv파일이어쓰기()

def csv파일읽기():
    f=open('sample.csv','r')
    rd = csv.reader(f)
    for row in rd:
        print(row)
    f.close()

csv파일읽기()
