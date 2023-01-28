# 문제1

lst = [10,20,30,40,50]

def 총합(a_lst):
    result = 0    # 함수 안에서 만든 변수는 함수가 끝나면 사라진다
    for i in lst:
        result += i
    return result

# result = return lst[0]+lst[1]+lst[2]+lst[3]


# =================================================================

sum = 총합(lst)
avg = sum/len(lst)

print('총합은',sum)
print('평균은',avg)


# 문제 2 : 입력한 갯수만큼 *을 표시하는 함수
def star(num): 
    result = ''
    for i in range(num):
        result += '*'

    return result

s1 = star(3)
s2 = star(5)
s3 = star()

print(s1)
print(s2)
print()





'''
별의 개수를 입력하시요 >>> 3
'''
