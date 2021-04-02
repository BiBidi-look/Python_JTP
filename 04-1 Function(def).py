
# 2021-04-01

'''
파이썬 함수의 구조
def 함수명(매개변수):   -> def 는 예약어(내가 이러한 함수를 이렇게 부를꺼야), *매개변수꼴일시, 부정(정해지지않은수의)매개변수에 적용가능. 
    <수행할 문장1>
    <수행할 문장2>
    ...
'''
print('='*50)

def add(a,b):    #여기서의 a,b는 매개변수(함수에 입력되는 값을 받아주는 변수)
    return a+b

a=3
b=4
c=add(a,b)
print(c)
print(add(5,6))  #여기서의 5,6은 인수(험수를 호출할때 전달하는 입력값)


def say():       #입력값이 없는 함수...A
    return 'Hi'

print(say())

'''
def add1(a,b):    #결과값(return)이 없는 함수...B
    print('%d, %d의 합은 %d입니다.'%(a,b,a+b))

add1(4,5) 

aa=add1(1,2)
print(aa)         #이것처럼 None(부정값)이 튀어나온다. 즉 수행은 하지만 return되는 값 자체가 존재하지 않기 때문에 벌어진 일이다.
'''

def say1():       #A와 B가 결합된, 입력값과 결과값 모두가 없는함수
    print("Hi")

say1()

def add2(a,b):
    return a+b

result=add2(b=10,a=15) #매개변수를 지정할시 순서를 좆대로해도 정상적으로 작동한다.
print(result)

def add_many(*args):
    result=0
    for i in args:
        result=result+i
    return result

result=add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice,*arg):
    if choice=="add":
        result=0
        for i in arg:
            result=result+i
    elif choice=="mul":
        result=1
        for i in arg:
            result=result*i
    return result

a=add_mul('add',1,2,3,4,5)
print(a)

print(add_mul('mul',1,2,3,4,5))

def print_kwargs(**kwargs): #**kwargs는 키워드 파라미터이다. 이는 a=b꼴로 투입시 이를 {'a':'b', ...}의 딕셔너리화 하는역할을 한다.
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo',age=3) #결과물처럼 모두 Dictionary형태로 출력된다.

def add_and_mul(a,b):
    return a+b, a*b         #결과값이 2개가 아닌, 튜플값 (a+b,a*b) 1개로 출력되는 형태이기 때문!

result=add_and_mul(3,4)
print(result)

'''
def add_and_mul1(a,b):
    return a+b
    return a*b  #return이 두개이기에 두번째 return은 작동하지 않는다.

result=add_and_mul1(3,5)
print(result)
'''

def say_nick(nick):
    if nick=="바보":
        return          #nick위치에 '바보'가 입력될시, 결과값을 반환하지않고 끝난다
    print("나의 별명은 %s입니다."%nick)     #그러나 그 이외는 입력된 값을 %s에 대입하여 출력한다 (출력하는 행동을 하는것이지, 결과값은 아니다)

say_nick('바보')

def say_myself(name,old,man=False):
    print('나의 이름은 %s입니다.'%name)
    print('나이는 %d살입니다.'%old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself('둘리',32)    #마지막 man의 참/거짓 여부항에 입력값이 없을경우, 초기 함수 정의시의 default값을 기본으로 한다
say_myself('둘리',32,True)
say_myself('둘리',32,'man')

'''
def say_myself1(name,man=False,old):
    print('나의 이름은 %s입니다.'%name)
    print('나이는 %d살입니다.'%old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself1('둘리',True,27)  #27이 man항에 들어갈지, old항에 들어갈지 판단하지 못하기에 오류가 발생한다.
                            #그러므로 초기화시킬매개변수는 항상 맨뒤에 놓아야한다.
'''


a=1                 #함수내에있지 않는 변수는 이름이 같다한들, 함수연산에 영향을 줄 수 없다.
def vartest(a):
    a+=1

print(a)            #그렇기에 그냥 1이 나온다.

'''
def vartest1(a):
    a = a + 1
vartest1(4)
print(a)         함수내의 a가 함수바깥에서 적용되지 않기때문에 오류가 발생한다
'''

a=1
def vartest2(A):
    A=A+1
    return A

a=vartest2(a)       #함수내의 A와 함수외의 a와는 다르다!
print(a)

b=10
def vartest3():
    global b        #함수바깥의 b를 그대로 가져와서 쓰는것. 하지만 이는 함수 정의의 독립성을 해치기때문에 비추
    b=b+1

vartest3()
print(b)

plus = lambda a,b:a+b   #def보다 간단한 형태의 함수를 만들어서 사용할때 lambda를 사용한다,
                        #lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식 꼴로 표현

result=plus(11,22)
print(result)






print('='*50)