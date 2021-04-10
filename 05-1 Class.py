
# 2021-04-05

print('='*50)


'''
result=0

def add(num):       #계산결과를 기억하는 덧셈계산기
    global result
    result += num
    return result

print(add(3))
print(add(5))
'''

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self,num):
        self.result+=num
        return self.result

cal1=Calculator()
cal2=Calculator()

print(cal1.add(3))
print(cal1.add(4))

print(cal2.add(30))
print(cal2.add(40))


class cookie:       #가장간단한 클레스.
    pass

a=cookie()          #위의 클레스를 이용하여 만든 객체. 각 객체 a,b는 서로 영향을 주지않는다. cookie라는 클레스에 의해 만들어졌을뿐이다.
b=cookie()          #쿠키라는 클레스를 이용해 만든 객체 = 인스턴스. ex) a는 cookie의 인스턴스(생산물이라고 볼 수 있겠다.)이며, a는 객체이다.


"""
class Fourcal:
    def setdata(self, first, second):   #클래스내부의 함수는 method라고 한다!
        self.first = first
        self.second = second
    def add(self):                      #매개변수를 self를 가져와서 계산한다.
        result = self.first + self.second   #객체 a기준으로는 a.first+a.second를 수행하는것이다.
        return result                       #a동을 통째로 가져와서 각 호수에 할당된 값을 이용하여 계산을 수행하는것이다!
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

'''
a=Fourcal()

print(type(a))    #Fourcal의 인스턴스인 a가 생성된것을 type(객체의 타입을 알려준다)를 통해 어떤 타입인지 확인했다.

a.setdata(2,4)    #3개가아닌 2개의 인자만 넣었는데, 이는 처음의 self에 setdata 메서드를 호출한 객체 a가 자동으로 넣어지기 때문이다.

#이때, 클레스를 직접 호출하는 식의 방법인 "Fourcal.setdata(a,2,4)"도 가능한데, 이땐 a가 꼭 있어야한다.
#set data를 호출하는 객체인 a가 할당되어야 하기 때문이다. (그래서 귀찮기땜에 잘안씀)

#여기서 a.setdata(2,4)에 의해 a.first=2 , a.second=4 의 형태로 객체 a에 각각의 객체변수 first,second가 생성되어 2,4가 각각 저장된다

print(a.first)  #a동2호, a동4호같은 느낌
print(a.second)
'''

a=Fourcal()
b=Fourcal()

a.setdata(4,2)
b.setdata(3,7)  #아주 중요하다. 각 객체에 객체변수2개씩을 지정했는데, 이는 독립적이며 서로 영향을 주지않는다.

print(id(a.first),id(b.first))  #a.first != b.first임을 다시금 확인한다. 위치자체가 다르다!

print(a.add())  #새로추가된 add메서드에 의해 a.first+b.first가 수행되어 출력되었다.
print(a.mul())  #4*2=8
print(b.sub())  #3-7=-4
print(b.div())  #3/7=0.43

"""

#생성자(Constructor)를 이용한 초기값부여

class Fourcal:
    def __init__(self, first, second):  #__init__을 이용하면 자동으로 객체의 초기값을 부여할 수 있다! (객체변수 first,second 생성!)
        self.first = first
        self.second = second
    def setdata(self, first, second):   
        self.first = first
        self.second = second
    def add(self):                      
        result = self.first + self.second   
        return result                       
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a=Fourcal(4,2)  #__init__에 의해 fourcal의 인스턴스인 a의 생성과 그 a의 객체변수 first, second를 생성했다. 
                #그렇기에 ()안에 first, second에 해당하는 값을 할당해야한다. self는 자동으로 a에 먹여졌기에 필요x

print(a.div()) #4/2=2 잘작동한다.

#클래스의 상속(inheritance). 어떤 클레스에 다른 클래스의 기능을 물려받는것. 원본클레스가 라이브러리형태 또는 수정불가상태라면 이를 이용한다.

class MoreFourcal(Fourcal): #신규 클레스명(상속받을 클레스명) 으로 상속시킨다.
    def pow(self):
        result = self.first ** self.second #a**b는 a^b와 같다는걸 잊지말자
        return result


a=MoreFourcal(3,2)
print(a.mul())   #fourcal의 메서드인 mul 기능을 그대로 사용할 수 있다!

print(a.pow())

#method overriding(덮어쓰기)

a=Fourcal(4,0)
#print(a.div())  -> 0으로 나누려고 해서 오류가 발생한다. 이를 수정해보자

class SafeFourcal(MoreFourcal):
    def div(self):                  #수정하고싶은 메서드와 동일한 이름으로 작성한다.
        if self.second==0:
            return 0
        else:
            return self.first/self.second

a=SafeFourcal(3,0)
print(a.div())  #기존 Fourcal의 div메서드가 아닌, SafeFourcal의 div메서드를 사용하여 계산한다. 0으로 나누려고해도 오류가 아닌, 0이나옴


#클레스변수

class Family:
    lastname="박"

print(Family.lastname) #family라는 클레스에서 lastname이라는 클레스의 변수를 호출했다.

a=Family()
b=Family()

print(a.lastname)
print(b.lastname) #lastname을 김->박으로 바꿀시, 각 객체의 a,b또한 바뀌었다.

print(id(a.lastname))
print(id(b.lastname))  #id도 같다










print('='*50)