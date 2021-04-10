
# 2021-04-06

print('='*50)

#파이썬 라이브러리는 자동으로 설치되어있다.


'''
-sys.argv : 파일이름.py you need python 이렇게 쓰면 sys.argv 리스트에 해당값이
['argv_test.py', 'you', 'need', 'python'] 이런식으로 추가된다.

sys.exit() : 스크립트 강종

sys.path : 모듈불러오기



'''

import pickle
f=open('test.txt','wb')         #딕셔너리 객체인자 data를 그대로 파일에 저장하는것.
data={1:'python',2:'you need'}
pickle.dump(data,f)
f.close

import pickle
f=open('test.txt','rb')
data=pickle.load(f)
print(data)                     #위에서 저장한 딕셔너리 객체인자 data를 다시 불러왔다


#OS모듈 -> 환경변수 디렉터리 파일등의 OS자원을 제어하는 모듈

import os
print(os.environ) #시스템환경변수값 여러가지를 딕셔너리 객체로써 보여준다

print(os.environ['PATH']) #PATH 환경변수값을 보여준다. 


# os.chdir("C:\WINDOWS") -> 디랙토리 위치 변경하기

print(os.getcwd()) #디랙토리 위치 돌려받기 (현재위치 정보를 반환)

'''
os.system*("**") -> 시스템 명령어 **을 실행한다
f = os.popen("**") -> 명령어 **을 수행한 결과값을 읽기모드 형태의 파일객체로써 돌려준다.
-> 읽기위해서는 당연히 print(f.read())를 해야한다
'''

import time
print(time.time()) #1970.1.1 00:00이후 지난시간을 초단위로 반환
print(time.localtime(time.time())) #위에서 돌려준 값을 연도 월 일...단위로 반환. 이는 튜플값으로 주어진다.
print(time.asctime()) #위에서 돌려준 튜플값을 보기쉬운형태로 다시 재구성했음
print(time.ctime()) #항상 현재시간만을 보여줌

#time.strftime('출력할 형식 포맷 코드', time.localtime(time.time())) -> 포멧코드에따라 시간을 세밀하게 표현함(https://wikidocs.net/33)

for i in range(10):
    print(i)
    time.sleep(0.1) #1초단위로 0~9까지으 숫자를 하나씩 출력한다. 즉 주어진 일정시간 간격으로 루프를 실행한다. 0.5를넣으면 0.5초단위가 된다

import calendar
print(calendar.prmonth(2021, 4)) #달력을 보여준다

import random
print(random.random()) #0~1.0 사이의 실수중, 난수값을 돌려준다
#random.randint(a,b)사용시, a~b사이의 정수중, 난수값을 돌려준다.

def random_pop(data):
    number = random.randint(0, len(data)-1) 
    return data.pop(number) #pop메서드에 의해 꺼낸결 과값은 사라진다

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]          #리스트내의 랜덤함수중, 주막위로 하나를 꺼내서 돌려준다.
    while data: 
        print(random_pop(data))

'''
import webbrowser
webbrowser.open("http://google.com") -> 구글페이지를 띄워준다

open->open_new 사용시 실행된 상태여도 새로운 창으로 띄운다
''' 


print('='*50)