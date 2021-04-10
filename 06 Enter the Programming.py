
# 2021-04-07

'''
06-1
def GuGu(n):
    result=[]
    i=1
    while i<10:
        result.append(n*i)
        i+=1
    return result

n=int(input('숫자를 입력하세요.:'))
print(GuGu(n))
'''

#10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
#1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

'''
06-2
result=0
for n in range(1,1000):
    if n%3==0 or n%5==0:            -> 주의해야할 점은 3의 배수와 5의 배수가 이중으로 더해지는 경우를 피하는것이다.
        result+=n
print(result)
'''

#Paging(게시판 페이지수를 보여주는 것)
#총 게시물수와 한페이지당 게시물수를 input했을때, 총페이지 수를 출력하는 프로그램을 작성

'''
def getTotalPage(m,n):  #m: 총 게시물수, n: 한페이지당 게시물 수
    return m//n+1

print(getTotalPage(5,10))
print(getTotalPage(30,10)) #문제발생! 30/10이면 딱떨어져서 3페이지가 되어야한다

def getTotalPage(m,n):
    if m%n==0:              #나머지가 0일 경우, 나눈값에 +1을 하지 않는 조건을 추가해주었다.
        return m//n
    else: m//n+1

print(getTotalPage(30,10))
'''

#메모장만들기
#기능: 메모추가/조회하기 //입력받는값:메모내용, 프로그램 실행 옵션 //출력하는 값: memo.txt

import sys

#sys.argv[0]->이는 생성할 메모파일의 파일명이므로 기능에 쓸 필요가없기에 1부터 시작한다.
'''
option = sys.argv[1]

if option=='-a':
    memo = sys.argv[2]
    f=open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close

elif option == '-v':
    f=option('memo.txt')
    memo=f.read()
    f.close
    print(memo)
'''

#06-6 os.listdir를 사용하면 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있다. ->이건 파일명만 나오고 확장자 안나옴
#os.path.join(dirname,file_name)을 사용하면 파일명과 디랙터리를 이어준다. ->파일 전체경로를 얻을 수 있음
#os.path.splitext는 파일 이름을 확장자를 기준으로 두 부분으로 나누어 준다.
#따라서 os.path.splitext(full_filename)[-1]은 해당 파일의 확장자 이름이 된다
'''
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):    ->해당 디랙터리파일이 또 디랙터리일경우 해당 경로를 다시금 검색하게했음
                                                    (search(ful_filename)->다시 search 함수에 들어가게됨)
                                                  이러한 방법을 재귀호출이라함.(자기자신을 다시 호출)
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py': 
                    print(full_filename)
    except PermissionError: -> 수행권한이 없는 디랙토리 접근시, 오류로 정지하지않고 pass시키기 위해 추가했음
        pass

search("c:/")

위의 과정을 os.walk매서드를 사용하면 더 편하게 작성할 수 있다.
(os.walk는 시작 디렉터리부터 시작하여 그 하위 모든 디렉터리를 차례대로 방문하게 해주는 함수)

import os

for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))
'''