
# 2021-04-02

print('='*50)

'''
f=open("newfile.txt",'w') #open은 내장함수로써 파일이름과 파일열기모드를 input하여, 파일객체를 output한다.
f.close()
'''

''' 
r:읽기모드(읽기만) w:쓰기모드 a:추가모드(파일의 마지막에 새로운내용 추가시 사용)
w는 파일이 존재할경우 원래 내용이 모두사라지며, 없다면 새로만든다.

'''

f=open("/Users/jeong-gyeonghun/Desktop/JTP/newfolder/newfile.txt",'w')
f.close


f=open('newfile.txt','w')
for i in range(1,11):
    data="%d번째줄입니다.\n" % i
    f.write(data)
f.close


f = open("/Users/jeong-gyeonghun/Desktop/JTP/newfile.txt", 'r')
while True:
    line = f.readline()     #readline자체가 순차적으로 순서를 기억하면서 출력하는 '함수'이다. (이너러블과 이너레이터에 의해 이너레이션이 구동)
    if not line:break
    print(line)
f.close()


print('동기화를 해보았다.')

# 2021-04-04

'''
while 1:
    data=input()
    if not data : break
    print(data)
'''

f = open("/Users/jeong-gyeonghun/Desktop/JTP/newfile.txt", 'r')
lines=f.readlines()     #readlines는 파일내 모든 줄을 읽고, 각 줄을 요소로하는 리스트를 반환한다. [1번쨰,2번째...etc]
for line in lines:
    print(line)
f.close()

f = open("/Users/jeong-gyeonghun/Desktop/JTP/newfile.txt", 'r')
data=f.read()   #파일의 내용 전체를 하나의 문자열로써 돌려준다. 1번째줄입니다.(\n)2번째줄입니다...이런식
                                                                #  ^ 2는 data[9]에 해당하게된다
print(data)
f.close()

f = open("/Users/jeong-gyeonghun/Desktop/JTP/newfile.txt", 'a')
for i in range(11,20):
    data = "%d번째 줄 입니다.\n" % i
    f.write(data)
f.close

with open("newfile.txt",'a') as f:
    f.write("Life is short, you need python.\n")

'''
import sys

args = sys.argv[1:]
for i in args:
    print(i)
'''



print('='*50)