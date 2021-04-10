
# 2021-04-06

print('='*50)

'''
f=open("emptyfile",'r')

print(4/0)

a=[1,2,3]
print(a[4])

위 3개는 빈번하게 일어나는 오류. 이를 무시하고 처리하는 방법은?

try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...
이 두가지 방법을 이용한다!

try블록 수행중 오류발생시 except블록을 수행한다.

이 방법은 3가지 종류가 있는데, 1) 오류종류 상관없이 except 수행 2) 지정 오류이름과 일치할때만 except수행 3) 2)+오류메시지 내용을 알려줌
'''

try:
    4/0
except ZeroDivisionError as e:
    print(e)
#4/0을 수행했기에 zerodivisionError가 나타나고, 그렇기에 해당 오류를 변수 e에 담아 이를 출력하게끔했다.

#try+finally절 사용 -> finally는 예외발생여부 상관없이 항상 수행한다. 그렇기에 f.close()와 같은 꼭 수행해야할 일을 여기에 배정하곤한다


try:
    f=open('test.txt', 'r')
    print(f.read())
finally:
    f.close()

#execpt는 try문 내에서 여러개를 배정할 수 있다.

try:
    a=[1,2,3]
    print(a[4])
    4/0
except ZeroDivisionError:
    print("0으로 나눌수 없다.")         #indexError가 먼저 발생했기에, zerodivisionError의 except는 수행되지 않았다.
except IndexError:
    print('없는것을 어떻게 말해')

try:
    a=[1,2,3]
    print(a[4])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
    a=[1,2,3]
    print(a[4])
    4/0
except (ZeroDivisionError,IndexError) as e: # 2개의 문제를 한번에 묶어서 같이 처리할 수도 있다. 아것또한 indexError만 발현!
    print(e)

#또한 else절도 사용가능하다
'''
try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...
else:  # 오류가 없을 경우에만 수행된다.
    ...
'''

try:
    age=int(input('나이를 입력하세요: ')) #int배정받을수있는 숫자만 입력을 해야한다.
except:
    print('숫자를 입력해주세요.')
else:
    if age <=18:
        print('민짜입니다.')
    else: print('성인입니다.')

#오류가 있을때 그냥 패스해야할때는? -> pass를 사용하면된다

try :
    f=open('emptyfile','r')
except FileNotFoundError: #FilenotfoundError만 패스한다. 만일 그냥 Except : pass일시 모든 오류를 패스한다.
    pass

#오류를 강제로 발생시켜야하는 경우?!

class Bird:
    def fly(self):      #bird클레스 상속시, fly함수를 반드시 수행하게함
        raise NotImplementedError  # NotImplementedError:파이썬 내장오류 - 필수요소 미구현일경우 일부러 오류를 일으키기위해 사용

class Eagle(Bird): #eagle클레스는 bird클레스를 상속받는다.
    #pass
    def fly(sely):         #1
        print('very fast') #2


eagle=Eagle() #eagle은 Eagle클레스에 속한다
eagle.fly()   #Eagle클레스가 상속받은 fly함수를 수행한다. -> 하지만 입력이 완전치 않아서 NotimplementedError를 발생!

#메서드 오버드라이빙을 통해 eagle클래스에 bird의 fly매서드를 수행하게끔 하기위해 pass를 삭제하고 #1, #2행을 추가한다.

#예외(exception)만들기 -> 특수경우에만 예외처리를 하기위함!

class MyError(Exception):
    #pass
    def __str__(self):                      #3
        return "허용되지 않는 별명입니다2."       #3

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

say_nick('멍청이') #멍청이는 출력되지만
#say_nick('바보')  #바보는 예외대상->myerror를 발생시킨다

try:
    say_nick("멍청이")
    say_nick("바보")
except MyError as e:
    print("허용되지 않는 별명입니다.")      #say_nick()함수에 바보라고 입력시, 이는 myerror를 유발하고, 
                                      #myerror는 예외사항으로 분류되어 허용되지 않는 별명이라는 문구를 출력한다.
    print(e)       #Myerror가 출력되어야 할거같지만 출력되지 않는다. 오류메세지를 출력하기위해서는 __str__메서드를 구현해야한다(#3)





print('='*50)